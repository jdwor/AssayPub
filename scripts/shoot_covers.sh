#!/bin/bash
# Screenshot pages of the built site. With no pages named, the cover of each edition.
# Usage: scripts/shoot_covers.sh <output folder> [width height [site folder [page path ...]]]
#   scripts/shoot_covers.sh shots 1280 800 preview editions/005/editorial/ works/openai-math-release/
cd "$(dirname "$0")/.."
OUT="${1:?output folder}"; W="${2:-1440}"; H="${3:-900}"; SITE="${4:-dist}"
shift 4 2>/dev/null || shift $#
mkdir -p "$OUT"
(cd "$SITE" && exec python3 -m http.server 8019 >/dev/null 2>&1) & SP=$!
trap 'kill $SP 2>/dev/null' EXIT
sleep 1
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ $# -eq 0 ]; then set -- $(cd "$SITE" && ls -d editions/[0-9]*/); fi
for page in "$@"; do
  n=$(echo "$page" | sed 's|/$||; s|/|-|g'); [ -z "$n" ] && n=home
  "$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=$W,$H --virtual-time-budget=5000 \
    --screenshot="$OUT/$n-$W.png" "http://127.0.0.1:8019/$page" >/dev/null 2>&1
  echo "$OUT/$n-$W.png"
done
