# /// script
# requires-python = ">=3.11"
# dependencies = ["jinja2>=3.1", "markdown-it-py>=3", "mdit-py-plugins>=0.4", "pillow>=10", "pyyaml>=6"]
# ///
"""Build the Assay site from content/.

    uv run site/build.py            # build what is public, into dist/: signed editions and the pilot
    uv run site/build.py --drafts   # the editor's preview, into preview/: draft editions as well
    uv run site/build.py --serve    # build, then serve the result on http://localhost:8017

dist/ is the folder that gets deployed, and only the public build writes to it.

Content model (all under content/):
    beats.yaml              the eight topics: rows of the cover and topic pages
    editions/<slug>.yaml    one edition: cover color, subject, editorial, funnel, shortlist, follow-ups
    works/<slug>.md         one selected work: front matter (the assessment) + Markdown body
    topics/<beat>.md        optional standing note for a topic page
    pages/<slug>.md         charter, method, corrections

The build validates every work and stops with a clear message if something is
missing or uses a term outside the controlled vocabulary.
"""
from __future__ import annotations

import datetime as dt
import functools
import http.server
import json
import os
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt
from markupsafe import Markup
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.footnote import footnote_plugin

from card import draw_card

ROOT = Path(__file__).resolve().parent.parent
CONTENT, SITE = ROOT / "content", ROOT / "site"
DRAFTS = "--drafts" in sys.argv
DIST = ROOT / ("preview" if DRAFTS else "dist")   # a preview never lands in the folder that is deployed

# ---- controlled vocabulary -------------------------------------------------
IMPORTANCE = ["Useful", "Notable", "Major", "Landmark"]          # weakest to strongest
EVIDENCE = ["Contested", "Preliminary", "Suggestive", "Solid", "Compelling", "Not applicable"]
NOVELTY = ["New capability", "New evidence", "New resource", "New framing", "New program",
           "Synthesis", "Audit or replication"]
INDEPENDENCE = ["Self-reported by developer", "Independent", "Peer-reviewed", "Not applicable"]
# The ratings a follow-up in a later edition may change, with the label each carries on the page.
RATINGS = {"importance": ("Importance", IMPORTANCE), "evidence": ("Evidence", EVIDENCE),
           "independence": ("Independence", INDEPENDENCE)}
CLAIM_STATUS = {"supported": "Supported", "self-reported": "Self-reported",
                "unverified": "Not verified", "disputed": "Disputed"}
REVIEW_STATUS = {"ai-drafted": "Drafted by {model}; not yet reviewed by an editor",
                 "editor-reviewed": "Drafted by {model}; reviewed and signed by the editor",
                 "author-responded": "Drafted by {model}; reviewed by the editor, with author response"}
TYPES = {"paper": "Paper", "lab-report": "Lab report", "essay": "Essay", "dataset": "Dataset",
         "software": "Software", "benchmark": "Benchmark", "model": "Model", "rfp": "Funding call",
         "initiative": "Initiative", "policy-report": "Policy report", "prize": "Prize",
         "fellowship": "Fellowship", "institute": "Institute", "compute-programme": "Compute programme",
         "link": "Link"}
# What a link beside an assessment is: the work's own material, someone else's response to it, or background.
LINK_KINDS = {"material": "More from the authors", "response": "Responses and critiques", "context": "Background"}
REQUIRED = ["title", "authors", "date", "type", "url", "beat", "edition", "well", "tier",
            "importance", "novelty", "evidence", "evidence_type", "independence", "checked", "standfirst"]
BIO_SLOT = "<!-- rows C and D -->"
# Cover colors, used in turn when an edition does not set `cover`. All take black ink. Chosen by the editor on
# November 18, 2026 in place of fully saturated versions of the same eight hues.
COVERS = ["#71cd99", "#e4ca69", "#f0a168", "#ef9fc5", "#7dc7f0", "#bcadf1", "#bddb6e", "#f39082"]
SOURCES = {"arxiv": "arXiv", "biorxiv": "bioRxiv", "nber": "NBER", "feeds": "Journals, labs and blogs",
           "huggingface": "Hugging Face", "github": "GitHub", "grants.gov": "Grants.gov", "bluesky": "Bluesky",
           "hackernews": "Hacker News"}

md = (MarkdownIt("commonmark", {"typographer": True, "html": True})
      .enable(["table", "strikethrough", "smartquotes"])
      .use(footnote_plugin).use(anchors_plugin, max_level=3))


def render_md(text):
    return Markup(md.render(text or ""))


def inline_md(text):
    return Markup(md.renderInline(str(text or "")))


def load_md(path):
    text = path.read_text()
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        return yaml.safe_load(fm) or {}, body.strip()
    return {}, text


def as_date(d):
    return d if isinstance(d, dt.date) else dt.date.fromisoformat(str(d)[:10])


def fmt_date(d, style="long"):
    if not d:
        return ""
    if isinstance(d, str) and len(d) == 7:  # month precision, e.g. 2026-09
        return dt.date.fromisoformat(d + "-01").strftime("%B %Y")
    d = as_date(d)
    return {"long": f"{d:%B} {d.day}, {d.year}", "short": f"{d:%B} {d.day}", "iso": d.isoformat(),
            "my": f"{d:%b %Y}"}[style]


def fail(msg):
    sys.exit(f"\nBuild stopped: {msg}\n")


# ---- load ------------------------------------------------------------------

def load():
    site = yaml.safe_load((ROOT / "site.yaml").read_text())
    # A deployment can supply the public address (the Pages workflow does); it takes precedence over site.yaml.
    site["url"] = (os.environ.get("ASSAY_URL") or site.get("url") or "").rstrip("/")
    beats = yaml.safe_load((CONTENT / "beats.yaml").read_text())
    by_slug = {b["slug"]: b for b in beats}

    works = []
    for p in sorted((CONTENT / "works").glob("*.md")):
        fm, body = load_md(p)
        w = {"slug": p.stem, **fm}
        missing = [k for k in REQUIRED if w.get(k) in (None, "", [])]
        if missing:
            fail(f"content/works/{p.name} is missing: {', '.join(missing)}")
        for field, vocab in (("importance", IMPORTANCE), ("novelty", NOVELTY), ("evidence", EVIDENCE),
                             ("independence", INDEPENDENCE)):
            if w[field] not in vocab:
                fail(f"content/works/{p.name}: {field} '{w[field]}' is not one of {vocab}")
        if w["beat"] not in by_slug:
            fail(f"content/works/{p.name}: unknown beat '{w['beat']}'")
        if w["type"] not in TYPES:
            fail(f"content/works/{p.name}: unknown type '{w['type']}'")
        # Every selected work records how fully it was read. A partial read must say what was missed.
        if w.get("read") not in ("full", "partial"):
            fail(f"content/works/{p.name}: needs `read: full`, or `read: partial` with a `read_gap`")
        if w["read"] == "partial" and not w.get("read_gap"):
            fail(f"content/works/{p.name}: `read: partial` needs a `read_gap`")
        for c in w.get("claims", []):
            if c.get("status") not in CLAIM_STATUS:
                fail(f"content/works/{p.name}: claim status '{c.get('status')}' is not one of {list(CLAIM_STATUS)}")
        w["edition"] = str(w["edition"])
        w["beat_obj"] = by_slug[w["beat"]]
        w["level"] = IMPORTANCE.index(w["importance"]) + 1
        w["_body"] = body
        w["type_label"] = TYPES[w["type"]]
        w["review_status"] = w.get("review_status", "ai-drafted")
        w["review_label"] = REVIEW_STATUS[w["review_status"]].format(model=w.get("drafted_by") or site["drafting_model"])
        for l in w.get("links") or []:
            if l.get("kind") not in LINK_KINDS:
                fail(f"content/works/{p.name}: link '{l.get('label')}' needs `kind`: one of {list(LINK_KINDS)}")
        w["links_by"] = {k: [l for l in w.get("links") or [] if l["kind"] == k] for k in LINK_KINDS}
        # `short` is the label printed on the cover. Without one the title is cut to fit.
        if not w.get("short"):
            print(f"  note: {p.name} has no `short` label; using the start of its title")
            w["short"] = " ".join(w["title"].split()[:5])
        if len(str(w["short"]).split()) > 5:
            fail(f"{p.name}: the cover title `short` has {len(str(w['short']).split())} words; the limit is five")
        w["col"] = int(w["well"][1:])
        w["address"] = f"{int(w['edition'])} · {w['well']}"
        works.append(w)

    editions = []
    for p in sorted((CONTENT / "editions").glob("*.yaml")):
        e = yaml.safe_load(p.read_text())
        e["slug"] = str(e.get("slug", p.stem))
        # `note` is the editorial. `note_bio`, the paragraph from the separate life-sciences pass,
        # goes where the editorial marks a place for it, or at the end if it marks none.
        note, bio = (e.get("note") or "").strip(), (e.get("note_bio") or "").strip()
        e["_note"] = note.replace(BIO_SLOT, bio) if BIO_SLOT in note else f"{note}\n\n{bio}"
        e["works"] = sorted([w for w in works if w["edition"] == e["slug"]], key=lambda w: (w["well"][0], w["col"]))
        for s in e.get("shortlist") or []:
            if s["beat"] not in by_slug:
                fail(f"{p.name}: shortlist entry '{s['title']}' has unknown beat '{s['beat']}'")
            s["beat_obj"], s["type_label"] = by_slug[s["beat"]], TYPES.get(s.get("type", "paper"), "Paper")
        e["plate"] = build_plate(e, beats, int(site.get("wells_per_row", 12)))
        for row in e["plate"]:
            row["works"] = sorted([w for w in e["works"] if w["beat"] == row["beat"]["slug"]], key=lambda w: w["col"])
        e["cover"] = e.get("cover") or COVERS[int(e["number"]) % len(COVERS)]
        e["period_label"] = period_label(e.get("period") or [])
        # Printed on the cover and in the archive once an editor has signed. Each assessment's own page
        # says who drafted it and whether it has been reviewed.
        e["status_short"] = f"Signed by {e['signed_by']}" if e.get("signed_by") else ""
        e["sources"] = [{"name": SOURCES.get(k, k), **v} for k, v in ((e.get("funnel") or {}).get("sources") or {}).items()]
        e["funnel"] = e.get("funnel") or {}
        e["funnel"]["selected"] = len(e["works"])
        e["funnel"]["shortlisted"] = len(e.get("shortlist") or [])   # shortlisted and not selected
        # `subject` names the editorial on the cover and in the archive: one to three words. Optional.
        e["subject"] = str(e.get("subject") or "").strip()
        if len(e["subject"].split()) > 4:
            fail(f"{p.name}: `subject` is a label of one to three words, not a headline ('{e['subject']}')")
        editions.append(e)
    # Text refers to another work or shortlist entry as {{key}}: a work's file name or a shortlist entry's `id`.
    # The build prints its well, with the edition number when it sits in a different edition, and links it.
    index = {w["slug"]: ("work", int(w["edition"]), w["well"], w["slug"]) for w in works}
    for e in editions:
        for s in e.get("shortlist") or []:
            if s.get("id"):
                index[s["id"]] = ("short", int(e["number"]), s["well"], e["slug"])

    def resolve(text, here, where):
        def one(m):
            hit = index.get(m.group(1))
            if not hit:
                fail(f"{where}: {{{{{m.group(1)}}}}} does not name a work or a shortlist entry")
            kind, n, well, ref = hit
            label = well if n == here else f"No. {n} · {well}"
            return f"[{label}](@root/works/{ref}/)" if kind == "work" else f"[{label}](@root/editions/{ref}/shortlist/#{well})"
        return re.sub(r"\{\{([\w-]+)\}\}", one, text or "")

    for w in works:
        here, where = int(w["edition"]), f"content/works/{w['slug']}.md"
        w["body"] = render_md(resolve(w.pop("_body"), here, where))
        for k in ("standfirst", "coi"):
            if w.get(k):
                w[k] = resolve(str(w[k]), here, where)
        for c in w.get("claims") or []:
            c["claim"], c["note"] = resolve(c["claim"], here, where), resolve(c.get("note", ""), here, where)
        for c in w.get("concerns") or []:
            c["body"], c["confidence"] = resolve(c["body"], here, where), resolve(c.get("confidence", ""), here, where)
    for e in editions:
        here, where = int(e["number"]), f"content/editions/{e['slug']}.yaml"
        e["note_html"] = render_md(resolve(e.pop("_note"), here, where))
        # The cover prints the first paragraph of the editorial.
        e["lead_html"] = render_md(resolve((e.get("note") or "").strip().split("\n\n")[0], here, where))
        for s in e.get("shortlist") or []:
            if s.get("note"):
                s["note"] = resolve(str(s["note"]), here, where)

    # A draft edition, and its assessments, stay out of the public build until the editor signs it.
    if not DRAFTS:
        editions = [e for e in editions if e.get("status") != "draft"]
    visible = {e["slug"] for e in editions}
    works = [w for w in works if w["edition"] in visible]

    # A follow-up reports a later development on a work from an earlier edition. It lives in the edition that
    # reports it. The earlier assessment is not edited: its page lists the follow-up, and a change of rating that
    # the follow-up records is applied here, with the rating as first published kept beside it.
    by_slug_w = {w["slug"]: w for w in works}
    for e in sorted(editions, key=lambda e: e["number"]):
        where, entries = f"content/editions/{e['slug']}.yaml", []
        for f in e.get("followups") or []:
            missing = [k for k in ("work", "date", "by", "url", "text") if not f.get(k)]
            if missing:
                fail(f"{where}: a follow-up is missing: {', '.join(missing)}")
            w = by_slug_w.get(f["work"])
            if not w:
                fail(f"{where}: follow-up names '{f['work']}', which is not an assessment in a public edition")
            if int(w["edition"]) >= int(e["number"]):
                fail(f"{where}: a follow-up on '{f['work']}' belongs in a later edition than the work itself")
            changes = []
            for field, new in (f.get("change") or {}).items():
                if field not in RATINGS or new not in RATINGS[field][1]:
                    fail(f"{where}: follow-up on '{f['work']}' cannot set {field} to '{new}'")
                if new != w[field]:
                    changes.append({"field": field, "label": RATINGS[field][0], "old": w[field], "new": new})
                    w.setdefault("first_rated", {}).setdefault(field, {"value": w[field], "until": e})
                    w[field] = new
            w["level"] = IMPORTANCE.index(w["importance"]) + 1
            entry = {"work": w, "edition": e, "date": f["date"], "by": f["by"], "url": f["url"], "changes": changes,
                     "text": inline_md(resolve(str(f["text"]), int(e["number"]), where))}
            entries.append(entry)
            w.setdefault("followups", []).append(entry)
        e["followups"] = entries
    editions.sort(key=lambda e: e["number"], reverse=True)
    for i, e in enumerate(editions):  # newest first, so the next edition is the one before it in the list
        e["next"] = editions[i - 1] if i else None
        e["prev"] = editions[i + 1] if i + 1 < len(editions) else None

    # A link to a work in an edition that is not public yet would lead nowhere, so it becomes plain text.
    shown = {w["slug"] for w in works}

    def unlink(html):
        html = re.sub(r'<a href="(?:@root/|(?:\.\./)+)works/([\w-]+)/">(.*?)</a>',
                      lambda m: m.group(0) if m.group(1) in shown else m.group(2), str(html))
        return Markup(re.sub(r'<a href="@root/editions/(\w+)/shortlist/#\w+">(.*?)</a>',
                             lambda m: m.group(0) if m.group(1) in visible else m.group(2), html))

    for w in works:  # inside an assessment, another work is linked as ../<slug>/
        w["body"] = Markup(re.sub(r'<a href="\.\./([\w-]+)/">(.*?)</a>',
                                  lambda m: m.group(0) if m.group(1) in shown else m.group(2), str(unlink(w["body"]))))
    for e in editions:
        e["note_html"], e["lead_html"] = unlink(e["note_html"]), unlink(e["lead_html"])
        for f in e["followups"]:
            f["text"] = unlink(f["text"])

    pages = {}
    for p in sorted((CONTENT / "pages").glob("*.md")):
        fm, body = load_md(p)
        pages[p.stem] = {"slug": p.stem, **fm, "body": render_md(body)}

    topics = {}
    for b in beats:
        tp = CONTENT / "topics" / f"{b['slug']}.md"
        fm, body = load_md(tp) if tp.exists() else ({}, "")
        topics[b["slug"]] = {**fm, "body": unlink(render_md(resolve(body, None, f"content/topics/{b['slug']}.md")))}

    charts = {}
    cp = ROOT / "data" / "charts" / "arxiv-volume.json"
    if cp.exists():
        charts = json.loads(cp.read_text())
    return site, beats, works, editions, pages, topics, charts


def period_label(period):
    """'July 2026' for a calendar month; otherwise 'July 1 – November 16, 2026'."""
    if len(period) != 2:
        return ""
    a, b = as_date(period[0]), as_date(period[1])
    if a.day == 1 and (a.year, a.month) == (b.year, b.month) and (b + dt.timedelta(days=1)).day == 1:
        return f"{a:%B} {a.year}"
    return f"{fmt_date(a, 'short' if a.year == b.year else 'long')} – {fmt_date(b)}"


def build_plate(edition, beats, wells=12):
    """Lay the edition out on a plate: one row per beat, `wells` wells per row (12 gives the 96-well plate)."""
    cells = {}

    def put(well, cell, what):
        m = re.fullmatch(r"([A-H])([1-9][0-9]?)", str(well))
        if not m or int(m.group(2)) > wells:
            fail(f"edition {edition['slug']}: '{well}' is not a well address (A1 to H{wells}) for {what}")
        if well in cells:
            fail(f"edition {edition['slug']}: well {well} is used twice ({what})")
        cells[well] = cell

    for w in edition["works"]:
        if w["well"][0] != w["beat_obj"]["row"]:
            fail(f"{w['slug']}: well {w['well']} is not in row {w['beat_obj']['row']} ({w['beat_obj']['name']})")
        put(w["well"], {"kind": "selected", "work": w}, w["slug"])
    for s in edition.get("shortlist") or []:
        put(s["well"], {"kind": "shortlisted", "entry": s}, s["title"])
    return [{"beat": b, "cells": [{"well": f"{b['row']}{c}", **cells.get(f"{b['row']}{c}", {"kind": "empty"})}
                                  for c in range(1, wells + 1)]} for b in beats]


# ---- write -----------------------------------------------------------------

def main():
    site, beats, works, editions, pages, topics, charts = load()
    env = Environment(loader=FileSystemLoader(SITE / "templates"),
                      autoescape=select_autoescape(["html", "xml"]), trim_blocks=True, lstrip_blocks=True)
    env.filters.update(date=fmt_date, md=render_md, mdi=inline_md,
                       tojson_compact=lambda o: Markup(json.dumps(o, separators=(",", ":"), default=str)))
    current = next((e for e in editions if e.get("status") != "hidden"), None)
    if not current:
        fail("no edition found in content/editions/")
    env.globals.update(site=site, beats=beats, editions=editions, current=current, CLAIM_STATUS=CLAIM_STATUS,
                       LINK_KINDS=LINK_KINDS,
                       build_date=dt.date.today(), year=dt.date.today().year)

    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(SITE / "static", DIST / "static")
    # The image a shared link shows: one card per edition, drawn from its plate (site/card.py).
    for e in editions:
        draw_card(e, site, DIST / "static" / "cards" / f"{e['slug']}.png")

    def page(path, template, **ctx):
        out = DIST / path
        out.parent.mkdir(parents=True, exist_ok=True)
        depth = len(Path(path).parts) - 1
        of = ctx.get("edition") or current
        ctx.setdefault("cover", of["cover"])
        root = "../" * depth or "./"
        if path == "404.html":   # served in place of any missing address, so its links start from the site's own path
            root = urlparse(site.get("url") or "").path.rstrip("/") + "/"
        # A page is shared with its edition's card. Link previews need full addresses, so these use the site's
        # address when it is known (it is in a deployment) and a relative path otherwise.
        card = f"static/cards/{of['slug']}.png"
        ctx.setdefault("card_url", f"{site['url']}/{card}" if site.get("url") else root + card)
        ctx.setdefault("card_alt", f"{site['name']} No. {of['number']}, {of['period_label']}: the edition's plate of selected and shortlisted works.")
        ctx.setdefault("page_url", f"{site['url']}/{path.removesuffix('index.html')}" if site.get("url") else "")
        out.write_text(env.get_template(template).render(root=root, path=path, **ctx).replace("@root/", root))

    # An edition is read in order, like an issue of a journal: its cover (the contents), the editorial, the list
    # of selected works, their assessments by well, the shortlist, and then the cover of the edition after it.
    # Each page of that run links to the one before and the one after.
    def step(href, label, title):
        return {"href": href, "label": label, "title": title}

    def reading_order(e):
        run = [step(f"editions/{e['slug']}/", "Contents", f"No. {e['number']} · {e['period_label']}"),
               step(f"editions/{e['slug']}/editorial/", "Editorial", e.get("subject") or e["title"])]
        count = lambda n: f"{n} work{'' if n == 1 else 's'}"
        if e["works"]:
            run.append(step(f"editions/{e['slug']}/selected/", "Selected", count(len(e["works"]))))
        run += [step(f"works/{w['slug']}/", w["well"], w["short"]) for w in e["works"]]
        if e.get("shortlist"):
            run.append(step(f"editions/{e['slug']}/shortlist/", "Shortlist", count(len(e["shortlist"]))))
        after = e.get("next")
        run.append(step(f"editions/{after['slug']}/", f"No. {after['number']}", after["period_label"]) if after else None)
        return {s["href"]: {"prev": run[i - 1], "next": run[i + 1]} for i, s in enumerate(run[:-1]) if i}

    page("index.html", "edition.html", edition=current, is_home=True, section="current")
    page("editions/index.html", "editions.html", section="editions")
    flow = {}
    for e in editions:
        flow.update(reading_order(e))
        page(f"editions/{e['slug']}/index.html", "edition.html", edition=e, is_home=False, section="editions")
        for part in ("editorial", "selected", "shortlist"):
            at = f"editions/{e['slug']}/{part}/"
            page(f"{at}index.html", "edition_part.html", edition=e, part=part, section="editions", **flow.get(at, {}))
    by_ed = {e["slug"]: e for e in editions}
    for w in works:
        e = by_ed.get(w["edition"]) or fail(f"{w['slug']}: edition '{w['edition']}' does not exist")
        page(f"works/{w['slug']}/index.html", "work.html", work=w, edition=e, section="editions", **flow[f"works/{w['slug']}/"])

    def topic_ctx(b):
        sel = [w for w in works if w["beat"] == b["slug"]]
        short = [dict(s, edition=e) for e in editions for s in (e.get("shortlist") or []) if s["beat"] == b["slug"]]
        chart = (charts.get("lenses") or {}).get(b["slug"])
        return {"beat": b, "selected": sorted(sel, key=lambda w: str(w["date"]), reverse=True),
                "shortlisted": short, "topic": topics[b["slug"]], "chart": chart,
                "chart_meta": {k: charts.get(k) for k in ("generated", "source", "note")}}

    page("topics/index.html", "topics.html", section="topics", topics=[topic_ctx(b) for b in beats])
    for b in beats:
        page(f"topics/{b['slug']}/index.html", "topic.html", section="topics", **topic_ctx(b))
    for slug, p in pages.items():
        page(f"{slug}/index.html", "page.html", page=p, section=slug)
    page("404.html", "page.html", section="", page={
        "title": "Page not found", "body": Markup("<p><a href='@root/'>Current edition</a></p>")})

    # Machine-readable twins.
    def followup_json(f):
        return {"work": f"assay:{f['work']['edition']}:{f['work']['well']}", "reported_in": f["edition"]["slug"],
                "date": str(f["date"]), "by": f["by"], "url": f["url"], "text": re.sub(r"<[^>]+>", "", str(f["text"])),
                "changes": {c["field"]: {"from": c["old"], "to": c["new"]} for c in f["changes"]}}

    def work_json(w):
        return {"id": f"assay:{w['edition']}:{w['well']}", "edition": w["edition"], "well": w["well"],
                "title": w["title"], "authors": w["authors"], "org": w.get("org", ""), "date": str(w["date"]),
                "type": w["type"], "url": w["url"], "license": w.get("license", ""), "beat": w["beat"],
                "tier": w["tier"], "assessment": {
                    "importance": w["importance"], "novelty": w["novelty"], "evidence": w["evidence"],
                    "evidence_type": w["evidence_type"], "independence": w["independence"],
                    "read": w["read"], "read_gap": w.get("read_gap", ""),
                    "checked": w["checked"], "conflicts": w.get("coi", ""), "review_status": w["review_status"],
                    "standfirst": w["standfirst"], "claims": w.get("claims", []), "concerns": w.get("concerns", []),
                    "first_published_as": {k: v["value"] for k, v in (w.get("first_rated") or {}).items()}},
                "followups": [followup_json(f) for f in w.get("followups") or []],
                "links": [{k: str(v) for k, v in l.items()} for l in w.get("links") or []],
                "page": f"{site['url']}/works/{w['slug']}/"}

    api = DIST / "api"
    api.mkdir()
    (api / "works.json").write_text(json.dumps([work_json(w) for w in works], indent=1, default=str)
                                    .replace("@root/", f"{site['url']}/"))
    (api / "editions.json").write_text(json.dumps([{
        "number": e["number"], "slug": e["slug"], "title": e["title"], "subject": e["subject"],
        "published": str(e.get("published", "")),
        "period": [str(x) for x in e.get("period", [])], "status": e.get("status", ""), "funnel": e["funnel"],
        "selected": [f"assay:{w['edition']}:{w['well']}" for w in e["works"]],
        "shortlisted": [{k: str(s.get(k, "")) for k in ("well", "title", "url", "org", "date", "type", "beat", "note")}
                        for s in (e.get("shortlist") or [])],
        "followups": [followup_json(f) for f in e["followups"]],
        "page": f"{site['url']}/editions/{e['slug']}/"} for e in editions], indent=1, default=str))
    page("feed.xml", "feed.xml", works=sorted(works, key=lambda w: str(w["date"]), reverse=True)[:60])
    page("llms.txt", "llms.txt", works=works)

    print(f"Built {len(editions)} edition(s), {len(works)} work page(s), {len(pages)} page(s) -> {DIST.name}/"
          + ("  (preview with drafts; not for deployment)" if DRAFTS else ""))
    if "--serve" in sys.argv:
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
        print("Serving http://localhost:8017  (Ctrl-C to stop)")
        http.server.ThreadingHTTPServer(("127.0.0.1", 8017), handler).serve_forever()


if __name__ == "__main__":
    main()
