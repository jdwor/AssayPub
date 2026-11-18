# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx>=0.27", "pypdf>=4", "pymupdf>=1.24", "pyyaml>=6"]
# ///
"""Check every quotation in the assessments against the documents it comes from.

    uv run editorial/check_quotes.py                 # all works
    uv run editorial/check_quotes.py navier-stokes-blowup
    uv run editorial/check_quotes.py --edition 001   # one edition's works

For each work in content/works/ this collects the passages in double quotation
marks (five words or more) from the body, standfirst, claims and concerns, then
fetches the work's `url` and every address under `links` and looks for each
passage in their text. A quotation found nowhere is reported, and the run exits
with an error so a draft edition cannot be signed with an unverified quotation.

A quotation taken from a source we could not open must be listed in the work's
front matter under `quotes_unverified`, and the text must say so in plain words.
Those are reported separately and do not fail the run.

Downloads are cached under data/cache/sources/ so re-runs are quick.
"""
import hashlib
import html
import io
import json
import re
import sys
import time
from pathlib import Path

import httpx
import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "cache" / "sources"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
MIN_WORDS = 5


def norm(s):
    """Fold typographic variants so a quotation matches its source."""
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"),
                 ("−", "-"), (" ", " "), (" ", " "), (" ", " "), ("ﬁ", "fi"), ("ﬂ", "fl"),
                 ("‑", "-"), ("­", "")):
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return re.sub(r" ([.,;:!?])", r"\1", s)  # markup in a source can leave a space before punctuation


def to_text(content, ctype, url):
    if content[:5] == b"%PDF-" or "pdf" in ctype or url.endswith(".pdf"):
        text = " ".join((p.extract_text() or "") for p in PdfReader(io.BytesIO(content)).pages)
        words = text.split()
        if words and sum(map(len, words)) / len(words) < 2.5:
            # Some PDFs come out of pypdf one letter at a time. Read those by position instead.
            import pymupdf
            text = " ".join(page.get_text("text") for page in pymupdf.open(stream=content, filetype="pdf"))
        return text
    s = content.decode("utf-8", "ignore")
    if "json" in ctype:  # API records: decode escapes such as \u2013 before reading
        try:
            s = json.dumps(json.loads(s), ensure_ascii=False)
        except ValueError:
            pass
    s = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", s)
    return html.unescape(re.sub(r"<[^>]+>", " ", s))


def expand(url):
    """The addresses worth reading for one link: the page itself plus fuller versions where they exist."""
    urls = [url]
    if m := re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", url):
        i = m.group(1)
        urls = [f"https://export.arxiv.org/api/query?id_list={i}", f"https://arxiv.org/html/{i}", f"https://arxiv.org/pdf/{i}"]
    elif m := re.fullmatch(r"https://github\.com/([^/]+/[^/]+)/?", url):
        urls += [f"https://raw.githubusercontent.com/{m.group(1)}/HEAD/README.md"]
    elif m := re.fullmatch(r"https://github\.com/([^/]+/[^/]+)/blob/(.+)", url):
        urls = [f"https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}"]
    return urls


def fetch(url):
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / (hashlib.sha256(url.encode()).hexdigest()[:20] + ".txt")
    if f.exists():
        return f.read_text()
    try:
        r = httpx.get(url, headers=UA, follow_redirects=True, timeout=60)
        if "arxiv.org" in url:
            time.sleep(3)
        text = to_text(r.content, r.headers.get("content-type", ""), url) if r.status_code == 200 else ""
    except Exception as e:  # a source that cannot be read is simply absent
        print(f"    could not read {url[:80]}: {type(e).__name__}")
        text = ""
    f.write_text(text)
    return text


def quotes_in(text):
    # Straight and curly quotation marks are paired separately, so a curly quotation inside a
    # straight one (a source quoting someone else) does not confuse the pairing.
    text = text or ""
    spans = re.findall(r'"([^"]{12,}?)"', text) + re.findall(r"“([^“”]{12,}?)”", text)
    return [s.strip() for s in spans if len(s.split()) >= MIN_WORDS]


def main():
    args = sys.argv[1:]
    edition = args[args.index("--edition") + 1] if "--edition" in args else None
    only = {a for a in args if not a.startswith("--") and a != edition}
    missing = 0
    for path in sorted((ROOT / "content" / "works").glob("*.md")):
        if only and path.stem not in only:
            continue
        _, fm, body = path.read_text().split("---", 2)
        w = yaml.safe_load(fm)
        if edition and str(w.get("edition")) != edition:
            continue
        parts = [body, str(w.get("standfirst", ""))]
        parts += [f"{c.get('claim', '')} {c.get('note', '')}" for c in w.get("claims") or []]
        parts += [f"{c.get('body', '')} {c.get('confidence', '')}" for c in w.get("concerns") or []]
        quotes = list(dict.fromkeys(q for p in parts for q in quotes_in(p)))
        if not quotes:
            continue
        declared = [norm(q) for q in w.get("quotes_unverified") or []]
        sources = [u for link in [w["url"], *[l["url"] for l in w.get("links") or []]] for u in expand(link)]
        corpus = norm(" ".join(fetch(u) for u in sources))
        ok = 0
        print(f"{path.stem}: {len(quotes)} quotation(s), {len(sources)} source address(es)")
        for q in quotes:
            n = norm(q)
            # Inner quotation marks and trailing punctuation differ between house style and source.
            bare = re.sub(r"[\"']", "", n).rstrip(".,;:")
            if n in corpus or bare in re.sub(r"[\"']", "", corpus):
                ok += 1
            elif any(n in d or d in n for d in declared):
                print(f"    declared unverified: “{q[:90]}”")
            else:
                missing += 1
                print(f"    NOT FOUND: “{q[:110]}”")
        print(f"    {ok} found")
    if missing:
        sys.exit(f"\n{missing} quotation(s) could not be found in their sources.")
    print("\nEvery quotation was found in its source or is declared unverified.")


if __name__ == "__main__":
    main()
