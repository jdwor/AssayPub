#!/bin/zsh
# Turn the monthly run on or off on this Mac. Nothing is scheduled until you run "install".
#
#   scripts/schedule.sh install     check at login and each morning; draft an edition once a month has ended
#   scripts/schedule.sh remove      stop
#   scripts/schedule.sh status
set -euo pipefail
LABEL="org.assay.monthly"
OLD="org.assay.weekly"            # the schedule's name while editions were weekly
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

case "${1:-status}" in
  install)
    mkdir -p "$HOME/Library/LaunchAgents" "$ROOT/data/runs"
    launchctl bootout "gui/$(id -u)/$OLD" 2>/dev/null || true
    rm -f "$HOME/Library/LaunchAgents/$OLD.plist"
    sed "s|__ROOT__|$ROOT|g" "$ROOT/scripts/monthly.plist.template" > "$PLIST"
    launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
    launchctl bootstrap "gui/$(id -u)" "$PLIST"
    echo "Scheduled. The run checks at login and at 06:00 daily (or at the next wake), and drafts an edition once a calendar month has ended." ;;
  remove)
    launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
    launchctl bootout "gui/$(id -u)/$OLD" 2>/dev/null || true
    rm -f "$PLIST" "$HOME/Library/LaunchAgents/$OLD.plist"
    echo "Removed." ;;
  status)
    launchctl print "gui/$(id -u)/$LABEL" 2>/dev/null | grep -E "state|last exit" || echo "Not scheduled." ;;
  *) echo "usage: scripts/schedule.sh install|remove|status"; exit 2 ;;
esac
