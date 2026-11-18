# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Number the wells of an edition, and merge the life-sciences pass into it.

    uv run editorial/assign_wells.py 001                       # assign any well still marked TBD
    uv run editorial/assign_wells.py 001 --bio data/runs/2026-11-22
    uv run editorial/assign_wells.py 000 --bio data/pilot/bio --rows C,D

Each topic is a plate row. Within a row, every item (selected or shortlisted) is
ordered by release date and numbered from 1. Rows that already have wells keep
them unless named in --rows.

With --bio, the folder's `bio-shortlist.yaml` replaces the edition's shortlist
for rows C and D, and `bio-note.md` becomes the edition's `note_bio`. The script
does not print the content it merges, so the main drafting model can run it
without reading the life-sciences material.
"""
import argparse
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BIO_BEATS = {"life-sciences", "chemistry-medicine"}


class Dumper(yaml.SafeDumper):
    pass


Dumper.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edition")
    ap.add_argument("--bio", help="folder holding bio-shortlist.yaml and bio-note.md from the life-sciences pass")
    ap.add_argument("--rows", default="", help="rows to renumber even if they already have wells, e.g. C,D")
    ap.add_argument("--drafted-by", default="", help="set drafted_by on life-sciences assessments that lack it")
    args = ap.parse_args()

    beats = yaml.safe_load((ROOT / "content" / "beats.yaml").read_text())
    row_of = {b["slug"]: b["row"] for b in beats}
    limit = int((yaml.safe_load((ROOT / "site.yaml").read_text()) or {}).get("wells_per_row", 12))
    path = ROOT / "content" / "editions" / f"{args.edition}.yaml"
    head = "".join(l for l in path.read_text().splitlines(keepends=True) if l.startswith("#"))
    ed = yaml.safe_load(path.read_text())
    if ed.get("status") == "published":
        sys.exit("That edition is signed; its wells are permanent.")
    force = {r.strip().upper() for r in args.rows.split(",") if r.strip()}
    shortlist = ed.get("shortlist") or []

    if args.bio:
        bio = ROOT / args.bio
        new = yaml.safe_load((bio / "bio-shortlist.yaml").read_text()) or []
        for s in new:
            if s.get("beat") not in BIO_BEATS:
                sys.exit(f"bio-shortlist.yaml: entry has beat '{s.get('beat')}', expected one of {sorted(BIO_BEATS)}")
            for k in ("title", "url", "date", "type"):
                if not s.get(k):
                    sys.exit(f"bio-shortlist.yaml: an entry is missing '{k}'")
            s["well"] = "TBD"
        shortlist = [s for s in shortlist if s["beat"] not in BIO_BEATS] + new
        note = bio / "bio-note.md"
        if note.exists():
            ed["note_bio"] = note.read_text().strip() + "\n"
        force |= {"C", "D"}

    works = []
    for p in sorted((ROOT / "content" / "works").glob("*.md")):
        text = p.read_text()
        fm = yaml.safe_load(text.split("---", 2)[1])
        if str(fm.get("edition")) == args.edition:
            works.append((p, fm))

    # Every shortlist entry has an id, so that text can refer to it as {{id}} whatever well it lands in.
    taken = {s["id"] for s in shortlist if s.get("id")} | {p.stem for p in (ROOT / "content" / "works").glob("*.md")}
    for other in (ROOT / "content" / "editions").glob("*.yaml"):
        if other != path:
            taken |= {x["id"] for x in (yaml.safe_load(other.read_text()).get("shortlist") or []) if x.get("id")}
    for s in shortlist:
        if not s.get("id"):
            words = [w for w in re.split(r"[^a-z0-9]+", unicodedata.normalize("NFKD", str(s["title"])).encode("ascii", "ignore").decode().lower()) if w]
            base = "-".join(words[:6])[:48].strip("-") or "item"
            key, i = base, 2
            while key in taken:
                key, i = f"{base}-{i}", i + 1
            s["id"] = key
            taken.add(key)

    selected_urls = {fm["url"] for _, fm in works}
    shortlist = [s for s in shortlist if s["url"] not in selected_urls]  # a selected work is not also shortlisted

    changed = 0
    for beat, row in row_of.items():
        items = [("work", p, fm) for p, fm in works if fm["beat"] == beat]
        items += [("short", s, s) for s in shortlist if s["beat"] == beat]
        if not items:
            continue
        if row not in force and all(re.fullmatch(rf"{row}[1-9][0-9]?", str(x[2].get("well", "")))
                                    and int(str(x[2]["well"])[1:]) <= limit for x in items):
            continue
        if len(items) > limit:
            sys.exit(f"Row {row} ({beat}) has {len(items)} items; the limit is {limit} (wells_per_row in site.yaml).")
        items.sort(key=lambda x: (str(x[2]["date"]), str(x[2]["title"])))
        for n, (kind, obj, data) in enumerate(items, 1):
            well = f"{row}{n}"
            if kind == "short":
                obj["well"] = well
            else:
                t = obj.read_text()
                t = re.sub(r"^well: .*$", f"well: {well}", t, count=1, flags=re.M)
                if args.drafted_by and beat in BIO_BEATS and not re.search(r"^drafted_by: ", t, re.M):
                    t = re.sub(r"^well: ", f"drafted_by: {args.drafted_by}\nwell: ", t, count=1, flags=re.M)
                obj.write_text(t)
            changed += 1
        print(f"row {row}: {len(items)} items numbered")

    order = {b["row"]: i for i, b in enumerate(beats)}
    shortlist.sort(key=lambda s: (order[s["well"][0]], int(s["well"][1:])))
    ed["shortlist"] = shortlist
    path.write_text(head + yaml.dump(ed, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=110))
    print(f"{changed} wells assigned; shortlist now has {len(shortlist)} items.")


if __name__ == "__main__":
    main()
