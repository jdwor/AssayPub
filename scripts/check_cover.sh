#!/bin/bash
# Check every cover of the built site for layout changes on hover, horizontal overflow and tooltips that leave
# the window, at several widths; at three widths check that a touch on a well shows its label as a bar, and that
# the list of editions under the number opens inside the window and is put away again. Builds first: the public
# site into dist/, or with --drafts the preview into preview/.
# Usage: scripts/check_cover.sh [--drafts]
set -e
cd "$(dirname "$0")/.."
OUT=dist; [ "$1" = "--drafts" ] && OUT=preview
uv run -q site/build.py "$@" > /dev/null
cp site/tests/hover.html site/tests/touch.html site/tests/menu.html "$OUT/"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if lsof -nP -iTCP:8018 -sTCP:LISTEN > /dev/null 2>&1; then echo "Port 8018 is in use; stop that server first." >&2; exit 1; fi
(cd "$OUT" && exec python3 -m http.server 8018 > /dev/null 2>&1) & SERVER=$!
trap 'kill $SERVER 2>/dev/null; wait $SERVER 2>/dev/null || true; if [ "$OUT" = dist ]; then uv run -q site/build.py > /dev/null; fi' EXIT   # leave dist/ without the test pages
sleep 1
for page in $(cd "$OUT/editions" && ls -d [0-9]*/ | sed 's|^|editions/|'); do
  for size in 1440,900 1280,800 1100,800 1024,768 900,800 700,800 520,800 390,844 320,700; do
    w=${size%,*}; h=${size#*,}
    "$CHROME" --headless=new --disable-gpu --virtual-time-budget=6000 --window-size=$((w+20)),$((h+60)) \
      --dump-dom "http://127.0.0.1:8018/hover.html?p=$page&w=$w&h=$h" 2>/dev/null | grep -o 'RESULT {[^<]*' || echo "RESULT none $page $w"
  done
  for size in 820,1180 390,844 320,700; do
    w=${size%,*}; h=${size#*,}
    "$CHROME" --headless=new --disable-gpu --virtual-time-budget=6000 --window-size=$((w+20)),$((h+60)) \
      --dump-dom "http://127.0.0.1:8018/touch.html?p=$page&w=$w&h=$h" 2>/dev/null | grep -o 'RESULT {[^<]*' || echo "RESULT none touch $page $w"
    "$CHROME" --headless=new --disable-gpu --virtual-time-budget=6000 --window-size=$((w+20)),$((h+60)) \
      --dump-dom "http://127.0.0.1:8018/menu.html?p=$page&w=$w&h=$h" 2>/dev/null | grep -o 'RESULT {[^<]*' || echo "RESULT none menu $page $w"
  done
done
