# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx>=0.27", "pypdf>=4", "pymupdf>=1.24", "pyyaml>=6"]
# ///
"""Read a web page or PDF as plain text, for checking facts against a source.

    uv run editorial/fetch.py <url>                       # first 6,000 characters
    uv run editorial/fetch.py <url> --grep "230.km"       # passages matching a pattern, with context
    uv run editorial/fetch.py <url> --max 40000 --offset 40000   # read a long text in parts

It only reads. It uses the same fetching and caching as check_quotes.py, so a
quotation confirmed here will pass that check.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_quotes import expand, fetch  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url")
    ap.add_argument("--grep", help="regular expression; print each match with surrounding text")
    ap.add_argument("--context", type=int, default=240, help="characters of context on each side of a match")
    ap.add_argument("--max", type=int, default=6000, help="characters to print when not using --grep")
    ap.add_argument("--offset", type=int, default=0, help="start printing at this character, to read a long text in parts")
    args = ap.parse_args()
    urls = expand(args.url)
    if "arxiv.org" in args.url and len(urls) == 3:
        # Metadata, then the full text once. arXiv's HTML rendering is cleaner but is sometimes
        # missing or cut short, so use it only when it is about as long as the PDF.
        meta, html_text, pdf_text = fetch(urls[0]), fetch(urls[1]), fetch(urls[2])
        text = meta + " " + (html_text if len(html_text) >= 0.7 * len(pdf_text) else pdf_text)
    else:
        text = " ".join(fetch(u) for u in urls)
    text = re.sub(r"\s+", " ", text)
    if not text.strip():
        sys.exit("Nothing could be read from that address.")
    if args.grep:
        hits = list(re.finditer(args.grep, text, re.I))
        print(f"{len(hits)} match(es) in {len(text):,} characters")
        for m in hits[:12]:
            print(f"@{m.start():,} …" + text[max(0, m.start() - args.context): m.end() + args.context] + "…\n")
    else:
        print(text[args.offset: args.offset + args.max])
        rest = len(text) - args.offset - args.max
        if rest > 0:
            print(f"\n[{rest:,} more characters of {len(text):,}; continue with --offset {args.offset + args.max}]")


if __name__ == "__main__":
    main()
