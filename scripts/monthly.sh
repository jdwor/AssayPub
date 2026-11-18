#!/bin/zsh
# The monthly run: scan, draft in two passes, merge, check, build a preview, notify.
# It never publishes, and it never writes to dist/ (the preview goes to preview/). See editorial/PROTOCOL.md.
#
#   scripts/monthly.sh                              the month that is due (see editorial/next_window.py)
#   scripts/monthly.sh 2026-11-01 2026-11-30 005    a given window and edition number
#
# Settings (environment variables):
#   ASSAY_MODEL           main pass                      default claude-fable-5-2
#   ASSAY_BIO_MODEL       life-sciences pass (rows C, D) default claude-opus-5; set to "none" to skip
#   ASSAY_BUDGET_USD      spending cap, main pass        default 100  (a month of reading; not yet measured)
#   ASSAY_BIO_BUDGET_USD  spending cap, second pass      default 40
#   ASSAY_USE_API_KEY=1   use ANTHROPIC_API_KEY instead of the Claude login
set -uo pipefail
cd "$(dirname "$0")/.."
export PATH="/opt/homebrew/bin:/usr/local/bin:$HOME/.local/bin:$PATH"

if (( $# >= 3 )); then
  SINCE=$1; UNTIL=$2; NNN=$3
else
  read -r SINCE UNTIL NNN <<< "$(uv run -q editorial/next_window.py)"
  if [[ "$SINCE" == "none" ]]; then echo "Nothing to do: $UNTIL $NNN"; exit 0; fi
fi
MODEL="${ASSAY_MODEL:-claude-fable-5-2}"
BIO_MODEL="${ASSAY_BIO_MODEL:-claude-opus-5}"
RUN="data/runs/$UNTIL"
mkdir -p "$RUN"
mkdir "$RUN/lock" 2>/dev/null || { echo "A run for the month ending $UNTIL is already in progress."; exit 0; }
trap 'rmdir "$RUN/lock" 2>/dev/null' EXIT

# After a wake the network can take a moment.
for i in {1..30}; do curl -s -m 5 -o /dev/null https://export.arxiv.org/ && break; sleep 10; done

CLAUDE=(claude)
[[ -z "${ASSAY_USE_API_KEY:-}" ]] && CLAUDE=(env -u ANTHROPIC_API_KEY -u ANTHROPIC_AUTH_TOKEN -u ANTHROPIC_BASE_URL claude)
# Each pass may read and write project files, search and read the web, and run these scripts. Nothing else.
TOOLS="Read,Write,Edit,Glob,Grep,WebSearch,WebFetch,ToolSearch,Skill"
TOOLS="$TOOLS,Bash(uv run monitor/list.py:*),Bash(uv run editorial/fetch.py:*),Bash(uv run editorial/check_quotes.py:*),Bash(uv run editorial/style_check.py:*)"
TOOLS="$TOOLS,Bash(uv run site/ingest_arxiv.py:*),Bash(uv run editorial/next_window.py:*)"
label() { case "$1" in claude-opus-5) echo "Claude Opus 5";; claude-fable-5-2) echo "Claude Fable 5.2";; *) echo "$1";; esac }

OK=1
{
  echo "== $(date) scan $SINCE to $UNTIL"
  uv run monitor/scan.py scan --since "$SINCE" --until "$UNTIL" || OK=0

  echo "== $(date) main pass ($MODEL)"
  "${CLAUDE[@]}" -p "Follow the instructions in .claude/skills/edition/SKILL.md. Arguments: $SINCE $UNTIL $NNN" --model "$MODEL" --permission-mode dontAsk \
    --allowedTools "$TOOLS" --max-budget-usd "${ASSAY_BUDGET_USD:-100}" < /dev/null || OK=0

  if [[ -f "content/editions/$NNN.yaml" ]]; then
    if [[ "$BIO_MODEL" != "none" ]]; then
      echo "== $(date) life-sciences pass ($BIO_MODEL)"
      "${CLAUDE[@]}" -p "Follow the instructions in .claude/skills/edition-bio/SKILL.md. Arguments: $SINCE $UNTIL $NNN" --model "$BIO_MODEL" --permission-mode dontAsk \
        --allowedTools "$TOOLS" --max-budget-usd "${ASSAY_BIO_BUDGET_USD:-40}" < /dev/null \
        || echo "The life-sciences pass did not finish; rows C and D may be empty."
    fi
    echo "== $(date) merge, check, build"
    if [[ -f "$RUN/bio-shortlist.yaml" ]]; then
      uv run editorial/assign_wells.py "$NNN" --bio "$RUN" --drafted-by "$(label "$BIO_MODEL")" || OK=0
    else
      uv run editorial/assign_wells.py "$NNN" || OK=0
    fi
    uv run editorial/check_quotes.py --edition "$NNN" || echo "Some quotations need attention before signing."
    uv run site/build.py --drafts || OK=0
  else
    echo "The main pass wrote no edition file."; OK=0
  fi
  echo "== $(date) finished"
} > "$RUN/run.log" 2>&1

if (( OK )); then touch "$RUN/done"; RESULT="Draft edition $NNN is ready. Reports are in $RUN/"; else RESULT="The monthly run had problems. See $RUN/run.log"; fi
osascript -e "display notification \"$RESULT\" with title \"Assay\"" 2>/dev/null || true
echo "$RESULT"
