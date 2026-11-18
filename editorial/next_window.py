# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""Say which month the next edition should cover, or that there is nothing to do.

    uv run editorial/next_window.py      ->  2026-11-01 2026-11-30 005
                                         or  none (reason)

Editions cover calendar months. The next window is the first month that no
edition covers to its end, and it is due once that month is over. So a late run
(the Mac was off on the 1st) still picks up the right month, and a run missed
for several months does the oldest first.

A draft that covers part of the month (the pilot left one for November 1 to 16)
is redone for the whole month under its own number. To test another date:
ASSAY_TODAY=2026-12-01 uv run editorial/next_window.py
"""
import datetime as dt
import os
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DAY = dt.timedelta(days=1)


def month_end(d):
    return (d.replace(day=28) + dt.timedelta(days=4)).replace(day=1) - DAY


def day(v):
    return dt.date.fromisoformat(str(v)[:10])


today = day(os.environ["ASSAY_TODAY"]) if os.environ.get("ASSAY_TODAY") else dt.date.today()
editions = [yaml.safe_load(p.read_text()) for p in sorted((ROOT / "content" / "editions").glob("*.yaml"))]
spans = [(day(e["period"][0]), day(e["period"][1]), e) for e in editions if e.get("period")]

# The last day covered by an edition that runs to the end of its month.
whole = [b for a, b, e in spans if b == month_end(b)]
since = max(whole) + DAY if whole else (today.replace(day=1) - DAY).replace(day=1)
until = month_end(since)
number = max((int(e["number"]) for e in editions), default=0) + 1

# Editions that stop inside the month: a draft is redone whole; anything already public is left as it is.
inside = [(a, b, e) for a, b, e in spans if since <= a <= until and b < until]
if inside and all(e.get("status") == "draft" for _, _, e in inside):
    number = min(int(e["number"]) for _, _, e in inside)
elif inside:
    since = max(b for _, b, _ in inside) + DAY

if until >= today:
    print(f"none ({since:%B %Y} is not over)")
elif (ROOT / "data" / "runs" / until.isoformat() / "done").exists():
    print(f"none (the run for {since:%B %Y} is finished)")
else:
    print(since, until, f"{number:03d}")
