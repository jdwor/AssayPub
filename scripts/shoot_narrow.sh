#!/bin/bash
# Screenshot a page of the preview at a phone width. Headless Chrome will not open a window narrower than about
# 500px, so the page is shown in a frame of the wanted width. A fifth argument scrolls the page first: a number of
# pixels, or "end" for the foot of the page.
# Usage: scripts/shoot_narrow.sh <output png> <width> <height> <page path> [scroll]
cd "$(dirname "$0")/.."
OUT="${1:?output png}"; W="${2:-390}"; H="${3:-844}"; PAGE="${4:-editions/004/}"; Y="${5:-0}"; [ "$Y" = end ] && Y=1e7
mkdir -p "$(dirname "$OUT")"
printf '<!doctype html><meta charset="utf-8"><style>html,body{margin:0;background:#888}iframe{border:0;display:block;width:%spx;height:%spx}</style><iframe src="%s" onload="this.contentWindow.scrollTo(0, %s)"></iframe>' "$W" "$H" "$PAGE" "$Y" > preview/_frame.html
(cd preview && exec python3 -m http.server 8019 >/dev/null 2>&1) & SP=$!
trap 'kill $SP 2>/dev/null' EXIT
sleep 1
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=$((W > 500 ? W : 500)),$H \
  --virtual-time-budget=5000 --screenshot="$OUT" "http://127.0.0.1:8019/_frame.html" >/dev/null 2>&1
echo "$OUT"
