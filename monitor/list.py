# /// script
# requires-python = ">=3.11"
# ///
"""Browse a candidates file without loading it whole.

    uv run monitor/list.py data/candidates/<window>/candidates.core.jsonl            # top 40 by score
    uv run monitor/list.py <file> --top 100 --offset 40
    uv run monitor/list.py <file> --grep "theorem|Lean" --beat mathematics-theory
    uv run monitor/list.py <file> --show arxiv:2609.19420                            # one record in full
"""
import argparse
import json
import re
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--grep", help="regular expression matched against title and abstract")
    ap.add_argument("--beat")
    ap.add_argument("--source")
    ap.add_argument("--show", help="print the full record with this id")
    a = ap.parse_args()
    rows = [json.loads(l) for l in open(a.file)]
    if a.show:
        hit = next((r for r in rows if r.get("id") == a.show), None)
        print(json.dumps(hit, indent=1, ensure_ascii=False) if hit else "No record with that id.")
        return
    if a.grep:
        pat = re.compile(a.grep, re.I)
        rows = [r for r in rows if pat.search(f"{r['title']} {r['abstract']}")]
    if a.beat:
        rows = [r for r in rows if r.get("beat") == a.beat]
    if a.source:
        rows = [r for r in rows if r.get("source") == a.source]
    print(f"{len(rows)} records; showing {a.offset + 1} to {min(len(rows), a.offset + a.top)}", file=sys.stderr)
    for r in rows[a.offset: a.offset + a.top]:
        print(f"{r.get('score', 0):5.1f} | {r['date'][:10]:10} | {r['source']:10} | {r.get('beat', '')[:18]:18} | {r['id']} | {r['title'][:110]}")


if __name__ == "__main__":
    main()
