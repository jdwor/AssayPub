# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Sign a draft edition. This is the only step that makes an edition public.

    uv run editorial/sign.py 001 --editor "Your Name"
    uv run editorial/sign.py 001 --editor "Your Name" --dry-run    # list what would be signed; change nothing

Run it after reading the draft against its sources. It checks every quotation
once more, marks the edition published, records who signed and when, and marks
each of its assessments as reviewed by the editor. Then rebuild and deploy.

Nothing is written unless every file can be updated: an edition with no
assessments, or an assessment whose front matter cannot be marked, stops the
script before any file changes.
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def front_matter(text):
    """The parsed front matter of an assessment, or {} if it has none."""
    if not text.startswith("---"):
        return {}
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def edition_of(text, width):
    """The edition an assessment names, as a slug. YAML reads an unquoted 004 as the number 4."""
    v = front_matter(text).get("edition")
    return "" if v is None else str(v).zfill(width)


def mark_reviewed(text):
    head, fm, body = text.split("---", 2)
    if re.search(r"^review_status:", fm, re.M):
        fm = re.sub(r"^review_status:.*$", "review_status: editor-reviewed", fm, count=1, flags=re.M)
    else:
        fm = fm.rstrip("\n") + "\nreview_status: editor-reviewed\n"
    return "---".join([head, fm, body])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edition", help="edition slug, e.g. 001")
    ap.add_argument("--editor", required=True, help="the signing editor's name, as it should appear")
    ap.add_argument("--skip-quote-check", action="store_true", help="sign without re-checking quotations")
    ap.add_argument("--dry-run", action="store_true", help="list the assessments that would be signed and stop")
    args = ap.parse_args()

    path = ROOT / "content" / "editions" / f"{args.edition}.yaml"
    if not path.exists():
        sys.exit(f"No such edition: {path.relative_to(ROOT)}")
    text = path.read_text()
    status = yaml.safe_load(text).get("status")
    if status == "published":
        sys.exit("That edition is already signed. Changes to it are corrections: see the corrections page.")

    works = [p for p in sorted((ROOT / "content" / "works").glob("*.md"))
             if edition_of(p.read_text(), len(args.edition)) == args.edition]
    if not works:
        sys.exit(f"Not signed: no assessment in content/works/ names edition {args.edition}.")
    print(f"Edition {args.edition}: {len(works)} assessments.")
    if args.dry_run:
        for p in works:
            print(f"  {p.stem}")
        print("Dry run: nothing was changed.")
        return

    if not args.skip_quote_check:
        check = subprocess.run(["uv", "run", "-q", str(ROOT / "editorial" / "check_quotes.py"), *[p.stem for p in works]])
        if check.returncode:
            sys.exit("Not signed: fix or declare the quotations above, then sign again.")

    # Prepare every change, confirm each took, and only then write.
    today = dt.date.today().isoformat()
    text = re.sub(r"^status: .*$", "status: published", text, count=1, flags=re.M)
    text = re.sub(r"^status_note: .*\n", "", text, count=1, flags=re.M)
    text = re.sub(r"^(signed_by|signed_on): .*\n", "", text, flags=re.M)
    text = text.rstrip("\n") + f"\nsigned_by: {args.editor}\nsigned_on: {today}\n"
    signed = yaml.safe_load(text)
    if signed.get("status") != "published" or signed.get("signed_by") != args.editor:
        sys.exit(f"Not signed: could not set the status in {path.relative_to(ROOT)}. Nothing was changed.")
    marked = {}
    for p in works:
        marked[p] = mark_reviewed(p.read_text())
        if front_matter(marked[p]).get("review_status") != "editor-reviewed":
            sys.exit(f"Not signed: could not mark {p.relative_to(ROOT)} as reviewed. Nothing was changed.")

    path.write_text(text)
    for p, t in marked.items():
        p.write_text(t)
    print(f"Edition {args.edition} signed by {args.editor} on {today}; {len(works)} assessments marked as reviewed.")
    print("Next: uv run site/build.py   then deploy dist/.")


if __name__ == "__main__":
    main()
