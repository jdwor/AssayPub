# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx>=0.27", "feedparser>=6", "pyyaml>=6"]
# ///
"""Assay monitor. Scans open sources for AI-for-science work in a date window.

    uv run monitor/scan.py scan --days 7                    # the weekly run
    uv run monitor/scan.py scan --since 2026-07-01 --until 2026-11-16 --label 2026-h2
    uv run monitor/scan.py scan --days 7 --only arxiv,feeds # some sources only
    uv run monitor/scan.py counts --from 2023-01            # monthly arXiv volume per beat (for topic charts)

Writes, under data/candidates/<label>/:
    raw/<source>.jsonl   every relevant record from each source
    candidates.jsonl     merged, de-duplicated, ranked by a cheap relevance score
    candidates.core.jsonl / candidates.bio.jsonl   the same list split for the two drafting passes
    funnel.json          how many records each source returned and how many passed

This stage only gathers and pre-ranks. Judging is the editorial stage's job
(see editorial/PROTOCOL.md). Sources and keywords live in monitor/sources.yaml.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import math
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import feedparser
import httpx
import yaml

ROOT = Path(__file__).resolve().parent.parent
UA = "AssayMonitor/0.1 (monthly research digest)"
client = httpx.Client(headers={"User-Agent": UA}, timeout=40, follow_redirects=True)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def get(url, *, tries=4, pause=2.0, **kw):
    """GET with retries. Returns the response, or None after `tries` failures."""
    for i in range(tries):
        try:
            r = client.get(url, **kw)
            if r.status_code == 200:
                return r
            if r.status_code in (403, 404):
                log(f"  {r.status_code} {url[:90]}")
                return None
        except httpx.HTTPError as e:
            log(f"  retry {i + 1}: {type(e).__name__} {url[:90]}")
        time.sleep(pause * (i + 1))
    return None


def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def item(source, **f):
    """One normalised candidate record."""
    return {
        "source": source,
        "found_via": [f.pop("via", source)],
        "type": f.pop("type", "paper"),
        "title": strip_tags(f.pop("title", "")),
        "authors": f.pop("authors", []),
        "org": f.pop("org", ""),
        "date": f.pop("date", ""),
        "url": f.pop("url", ""),
        "abstract": strip_tags(f.pop("abstract", ""))[:3000],
        "license": f.pop("license", ""),
        "beat": f.pop("beat", ""),
        "signals": f.pop("signals", {}),
        **f,
    }


# ------------------------------------------------------------------ relevance

class Relevance:
    def __init__(self, cfg, lenses):
        self.cfg, self.lenses = cfg, lenses

    def score(self, text):
        t = f" {text} "
        low = t.lower()
        strong = sum(1 for p in self.cfg["strong"] if p.lower() in low)
        # Short upper-case terms such as " AI " are matched case-sensitively.
        ai = any((p in t) if p.strip(" -").isupper() else (p.lower() in low) for p in self.cfg["ai_terms"])
        sci = sum(1 for p in self.cfg["science_terms"] if p.lower() in low)
        return min(strong, 3) * 3 + (2 if ai and sci else 0) + (1 if ai and sci >= 3 else 0)

    def beat(self, text):
        low = text.lower()
        best, hits = "", 0
        for name, lens in self.lenses.items():
            if name == "general":
                continue
            n = sum(1 for p in lens["any"] if p.lower() in low)
            if n > hits:
                best, hits = name, n
        return best


# ------------------------------------------------------------------ arXiv

ARXIV = "https://export.arxiv.org/api/query"


def arxiv_query(lens, since, until):
    def group(ps):
        return "(" + " OR ".join(f'abs:"{p}"' for p in ps) + ")"
    q = group(lens["any"])
    if lens.get("and"):
        q += " AND " + group(lens["and"])
    return f"{q} AND submittedDate:[{since:%Y%m%d}0000 TO {until:%Y%m%d}2359]"


def arxiv_page(q, start):
    """One page of results. Under load arXiv sometimes answers with an empty feed, so empty pages are retried."""
    feed = None
    for attempt in range(4):
        r = get(ARXIV, params={"search_query": q, "start": start, "max_results": 200,
                               "sortBy": "submittedDate", "sortOrder": "descending"})
        time.sleep(3.1)  # arXiv asks for three seconds between calls
        feed = feedparser.parse(r.text) if r else None
        if feed and feed.entries:
            return feed
        time.sleep(6 * (attempt + 1))
    return feed


def scan_arxiv(cfg, since, until, stats):
    for name, lens in cfg["lenses"].items():
        q, start, total = arxiv_query(lens, since, until), 0, None
        while total is None or start < total:
            feed = arxiv_page(q, start)
            if not feed or not feed.entries:
                break
            total = int(feed.feed.get("opensearch_totalresults", 0))
            for e in feed.entries:
                m = re.search(r"abs/([\d.]+)(v\d+)?", e.id)
                aid = m.group(1) if m else e.id
                stats["scanned"] += 1
                yield item("arxiv", via=f"arxiv:{name}", title=e.title, abstract=e.summary,
                           authors=[a.name for a in e.get("authors", [])],
                           date=e.published[:10], url=f"https://arxiv.org/abs/{aid}",
                           beat="" if name == "general" else name,
                           category=e.get("arxiv_primary_category", {}).get("term", ""),
                           arxiv_id=aid)
            start += 200
        log(f"  arxiv/{name}: {total or 0}")


def arxiv_counts(cfg, first_month, out):
    """Monthly count of arXiv preprints matching each lens. Powers the topic-page charts."""
    today = dt.date.today()
    months, y, m = [], *map(int, first_month.split("-"))
    while (y, m) <= (today.year, today.month):
        months.append((y, m))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    result = {"generated": today.isoformat(), "source": "arXiv API, opensearch:totalResults",
              "note": "Count of preprints first submitted in the month whose abstract matches the lens.",
              "lenses": {}}
    for name, lens in cfg["lenses"].items():
        rows = []
        for (y, m) in months:
            a = dt.date(y, m, 1)
            b = (dt.date(y + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1))
            partial = b > today
            n = None
            for _ in range(3):
                r = get(ARXIV, params={"search_query": arxiv_query(lens, a, min(b, today)), "max_results": 1})
                time.sleep(3.1)
                if r:
                    f = feedparser.parse(r.text)
                    if "opensearch_totalresults" in f.feed:
                        n = int(f.feed["opensearch_totalresults"])
                        break
            rows.append({"month": f"{y}-{m:02d}", "count": n, "partial": partial})
            log(f"  {name} {y}-{m:02d}: {n}")
        result["lenses"][name] = {"any": lens["any"], "and": lens.get("and", []), "months": rows}
        out.write_text(json.dumps(result, indent=1))  # save progress after each lens
    return result


# ------------------------------------------------------------------ bioRxiv / medRxiv

def scan_biorxiv(cfg, since, until, stats):
    kws = [k.lower() for k in cfg["keywords"]]
    lic = {"cc_by": "CC BY 4.0", "cc_by_nc": "CC BY-NC 4.0", "cc_by_nd": "CC BY-ND 4.0",
           "cc_by_nc_nd": "CC BY-NC-ND 4.0", "cc0": "CC0", "cc_no": "No reuse"}
    for server in cfg["servers"]:
        base = f"https://api.biorxiv.org/details/{server}/{since}/{until}"
        first = get(f"{base}/0/json")
        if not first:
            continue
        msg = first.json()["messages"][0]
        total, page = int(msg.get("total", 0)), int(msg.get("count", 100)) or 100
        log(f"  {server}: {total} records, {page} per page")

        def fetch(cursor):
            r = get(f"{base}/{cursor}/json")
            return r.json().get("collection", []) if r else []

        with ThreadPoolExecutor(max_workers=4) as pool:
            for coll in pool.map(fetch, range(0, total, page)):
                for rec in coll:
                    if str(rec.get("version")) != "1":
                        continue  # revisions of older preprints are not new work
                    stats["scanned"] += 1
                    text = f"{rec['title']} {rec['abstract']}".lower()
                    if not any(k in text for k in kws):
                        continue
                    yield item(server, title=rec["title"], abstract=rec["abstract"],
                               authors=[a.strip() for a in rec["authors"].split(";")][:12],
                               org=rec.get("author_corresponding_institution", ""),
                               date=rec["date"], url=f"https://doi.org/{rec['doi']}",
                               license=lic.get(rec.get("license", ""), rec.get("license", "")),
                               category=rec.get("category", ""), doi=rec["doi"])


# ------------------------------------------------------------------ NBER

MONTHS = {m: i for i, m in enumerate(
    "January February March April May June July August September October November December".split(), 1)}


def scan_nber(cfg, since, until, stats):
    kws = [k.lower() for k in cfg["keywords"]]
    for page in range(1, 40):
        r = get("https://www.nber.org/api/v1/working_page_listing/contentType/working_paper/_/_/search",
                params={"page": page, "perPage": 100, "sortBy": "public_date"})
        if not r:
            break
        older = 0
        for w in r.json().get("results", []):
            mname, _, year = (w.get("displaydate") or "").partition(" ")
            if mname not in MONTHS or not year.isdigit():
                continue
            month = dt.date(int(year), MONTHS[mname], 1)
            if month < since.replace(day=1):
                older += 1
                continue
            if month > until:
                continue
            stats["scanned"] += 1
            text = f" {w['title']} {w.get('abstract', '')} "
            low = text.lower()
            if not any((k in text) if k.strip().isupper() else (k in low) for k in kws):
                continue
            yield item("nber", title=w["title"], abstract=w.get("abstract", ""),
                       authors=[strip_tags(a) for a in w.get("authors", [])],
                       date=month.isoformat()[:7], url="https://www.nber.org" + w["url"],
                       beat="science-of-science", date_precision="month")
        if older >= 90:
            break
        time.sleep(1)


# ------------------------------------------------------------------ feeds and sitemaps

def entry_date(e):
    t = e.get("published_parsed") or e.get("updated_parsed")
    return dt.date(*t[:3]) if t else None


def scan_feeds(cfg, since, until, stats, rel):
    kinds = {"labs": "lab-report", "newsletters": "essay", "funders": "rfp"}
    for group, feeds in cfg.items():
        for f in feeds:
            r = get(f["url"], tries=2)
            if not r:
                log(f"  feed failed: {f['name']}")
                continue
            n = 0
            if f["kind"] == "sitemap":
                pat = re.compile(f["include"])
                for loc, mod in re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", r.text):
                    if not pat.search(loc) or not (since.isoformat() <= mod[:10] <= until.isoformat()):
                        continue
                    stats["scanned"] += 1
                    page = get(loc, tries=2)
                    if not page:
                        continue
                    title = re.search(r"<title[^>]*>([^<]+)</title>", page.text)
                    desc = re.search(r'<meta[^>]+(?:name="description"|property="og:description")[^>]+content="([^"]*)"',
                                     page.text)
                    pub = re.search(r'"(?:datePublished|publishedOn|publishedAt)"\s*:\s*"(\d{4}-\d{2}-\d{2})', page.text)
                    yield item("feeds", via=f"{group}:{f['name']}", type=f.get("type", kinds[group]),
                               title=title.group(1) if title else loc, abstract=desc.group(1) if desc else "",
                               org=f["name"], date=pub.group(1) if pub else mod[:10], url=loc,
                               date_kind="published" if pub else "last-modified", feed_filter=f["filter"])
                    n += 1
                    time.sleep(0.3)
            else:
                for e in feedparser.parse(r.text).entries:
                    d = entry_date(e)
                    if not d or not (since <= d <= until):
                        continue
                    stats["scanned"] += 1
                    body = e.get("summary", "") or (e.get("content") or [{}])[0].get("value", "")
                    yield item("feeds", via=f"{group}:{f['name']}", type=f.get("type", kinds[group]),
                               title=e.get("title", ""), abstract=body,
                               authors=[e["author"]] if e.get("author") else [],
                               org=f["name"], date=d.isoformat(), url=e.get("link", ""),
                               feed_filter=f["filter"])
                    n += 1
            log(f"  {group}/{f['name']}: {n}")


# ------------------------------------------------------------------ social signals

def scan_bluesky(cfg, since, until, stats):
    for q in cfg["queries"]:
        r = get("https://api.bsky.app/xrpc/app.bsky.feed.searchPosts", tries=2,
                params={"q": q, "sort": "top", "limit": 100,
                        "since": f"{since}T00:00:00Z", "until": f"{until}T23:59:59Z"})
        if not r:
            continue
        for p in r.json().get("posts", []):
            stats["scanned"] += 1
            likes = p.get("likeCount", 0)
            if likes < cfg["min_likes"]:
                continue
            rec = p.get("record", {})
            links = [f["features"][0].get("uri") for f in rec.get("facets", [])
                     if f.get("features") and f["features"][0].get("uri")]
            ext = (p.get("embed") or {}).get("external") or {}
            if ext.get("uri"):
                links.append(ext["uri"])
            if not links:
                continue
            handle = p["author"]["handle"]
            yield {"network": "bluesky", "author": handle, "text": rec.get("text", "")[:400],
                   "links": list(dict.fromkeys(links)), "likes": likes, "reposts": p.get("repostCount", 0),
                   "date": rec.get("createdAt", "")[:10], "title": ext.get("title", ""),
                   "url": f"https://bsky.app/profile/{handle}/post/{p['uri'].rsplit('/', 1)[-1]}"}
        time.sleep(1)


def scan_hackernews(cfg, since, until, stats):
    a = int(dt.datetime.combine(since, dt.time(), dt.timezone.utc).timestamp())
    b = int(dt.datetime.combine(until, dt.time(23, 59), dt.timezone.utc).timestamp())
    for q in cfg["queries"]:
        r = get("https://hn.algolia.com/api/v1/search", tries=2,
                params={"query": q, "tags": "story", "hitsPerPage": 100,
                        "numericFilters": f"created_at_i>{a},created_at_i<{b},points>{cfg['min_points']}"})
        if not r:
            continue
        for h in r.json().get("hits", []):
            stats["scanned"] += 1
            if not h.get("url"):
                continue
            yield {"network": "hackernews", "author": h.get("author", ""), "text": "", "title": h.get("title", ""),
                   "links": [h["url"]], "points": h.get("points", 0), "comments": h.get("num_comments", 0),
                   "date": h.get("created_at", "")[:10],
                   "url": f"https://news.ycombinator.com/item?id={h['objectID']}"}
        time.sleep(0.5)


# ------------------------------------------------------------------ datasets, models, software

def scan_huggingface(cfg, since, until, stats):
    seen = set()
    for kind in ("datasets", "models"):
        for tag in cfg["tags"]:
            r = get(f"https://huggingface.co/api/{kind}", tries=2,
                    params={"filter": tag, "sort": "likes", "direction": -1, "limit": 500, "full": "true"})
            if not r:
                continue
            for d in r.json():
                stats["scanned"] += 1
                created = (d.get("createdAt") or "")[:10]
                if d["id"] in seen or not (since.isoformat() <= created <= until.isoformat()):
                    continue
                if d.get("likes", 0) < cfg["min_likes"]:
                    continue
                seen.add(d["id"])
                card = d.get("cardData") or {}
                lic = card.get("license", "")
                yield item("huggingface", via=f"huggingface:{tag}", type=kind[:-1], title=d["id"],
                           org=d.get("author", ""), date=created,
                           url=f"https://huggingface.co/{'datasets/' if kind == 'datasets' else ''}{d['id']}",
                           abstract=" ".join(map(str, card.get("tags", []) or d.get("tags", [])))[:600],
                           license=", ".join(lic) if isinstance(lic, list) else str(lic),
                           beat="infrastructure",
                           signals={"hf_likes": d.get("likes", 0), "hf_downloads": d.get("downloads", 0)})
            time.sleep(0.5)


def scan_github(cfg, since, until, stats):
    seen = set()
    for q in cfg["queries"]:
        r = get("https://api.github.com/search/repositories", tries=2, pause=20,
                params={"q": f"{q} created:{since}..{until} stars:>={cfg['min_stars']}",
                        "sort": "stars", "order": "desc", "per_page": 50},
                headers={"Accept": "application/vnd.github+json"})
        time.sleep(7)  # unauthenticated search allows ten calls a minute
        if not r:
            continue
        for repo in r.json().get("items", []):
            stats["scanned"] += 1
            if repo["full_name"] in seen:
                continue
            seen.add(repo["full_name"])
            yield item("github", via=f"github:{q}", type="software", title=repo["full_name"],
                       org=repo["owner"]["login"], date=repo["created_at"][:10], url=repo["html_url"],
                       abstract=repo.get("description") or "",
                       license=(repo.get("license") or {}).get("spdx_id", "") or "",
                       beat="infrastructure", signals={"github_stars": repo["stargazers_count"]})


def scan_grants_gov(cfg, since, until, stats):
    seen = set()
    for kw in cfg["keywords"]:
        try:
            r = client.post("https://api.grants.gov/v1/api/search2",
                            json={"keyword": kw, "oppStatuses": "posted|forecasted", "rows": 200})
            hits = r.json()["data"]["oppHits"]
        except Exception as e:  # the endpoint is occasionally down
            log(f"  grants.gov failed: {e}")
            continue
        for h in hits:
            stats["scanned"] += 1
            try:
                opened = dt.datetime.strptime(h.get("openDate", ""), "%m/%d/%Y").date()
            except ValueError:
                continue
            if h["id"] in seen or not (since <= opened <= until):
                continue
            seen.add(h["id"])
            yield item("grants.gov", type="rfp", title=h["title"], org=h.get("agency", ""),
                       date=opened.isoformat(), url=f"https://www.grants.gov/search-results-detail/{h['id']}",
                       abstract=f"{h.get('number', '')}. Closes {h.get('closeDate') or 'not stated'}.",
                       beat="institutions", deadline=h.get("closeDate", ""))
        time.sleep(1)


# ------------------------------------------------------------------ merge

def key(url, title=""):
    """A stable identity for de-duplication across sources."""
    if m := re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", url):
        return "arxiv:" + m.group(1)
    if m := re.search(r"(10\.\d{4,9}/[^\s?#]+)", url):
        return "doi:" + m.group(1).rstrip("/").removesuffix(".full").removesuffix(".pdf").lower()
    u = re.sub(r"^https?://(www\.)?", "", url.split("#")[0])
    u = re.sub(r"[?&](utm_[^&]+|ref=[^&]+|from=[^&]+)", "", u).rstrip("/?").lower()
    return "url:" + u if u else "title:" + re.sub(r"\W+", "", title.lower())[:80]


def run_scan(args):
    cfg = yaml.safe_load((ROOT / "monitor" / "sources.yaml").read_text())
    until = dt.date.fromisoformat(args.until) if args.until else dt.date.today()
    since = dt.date.fromisoformat(args.since) if args.since else until - dt.timedelta(days=args.days)
    out = ROOT / "data" / "candidates" / (args.label or f"{since}_{until}")
    (out / "raw").mkdir(parents=True, exist_ok=True)
    rel = Relevance(cfg["relevance"], cfg["arxiv"]["lenses"])
    only = set(args.only.split(",")) if args.only else None
    log(f"Scanning {since} to {until} -> {out.relative_to(ROOT)}")

    scanners = {
        "arxiv": lambda s: scan_arxiv(cfg["arxiv"], since, until, s),
        "biorxiv": lambda s: scan_biorxiv(cfg["biorxiv"], since, until, s),
        "nber": lambda s: scan_nber(cfg["nber"], since, until, s),
        "feeds": lambda s: scan_feeds(cfg["feeds"], since, until, s, rel),
        "huggingface": lambda s: scan_huggingface(cfg["resources"]["huggingface"], since, until, s),
        "github": lambda s: scan_github(cfg["resources"]["github"], since, until, s),
        "grants.gov": lambda s: scan_grants_gov(cfg["grants_gov"], since, until, s),
    }
    socials = {
        "bluesky": lambda s: scan_bluesky(cfg["social"]["bluesky"], since, until, s),
        "hackernews": lambda s: scan_hackernews(cfg["social"]["hackernews"], since, until, s),
    }

    funnel = json.loads((out / "funnel.json").read_text()) if (out / "funnel.json").exists() else {"sources": {}}
    threshold = cfg["relevance"]["threshold"]

    for name, scanner in scanners.items():
        if only and name not in only:
            continue
        log(f"[{name}]")
        stats, kept = {"scanned": 0}, []
        for it in scanner(stats):
            text = f"{it['title']} {it['abstract']}"
            it["relevance"] = rel.score(text)
            it["beat"] = it["beat"] or rel.beat(text)
            # arXiv, HF, GitHub and grants.gov are already keyword-matched at the source.
            always = name in ("arxiv", "huggingface", "github", "grants.gov") or it.pop("feed_filter", "") == "all"
            if always or it["relevance"] >= threshold:
                kept.append(it)
        (out / "raw" / f"{name}.jsonl").write_text("".join(json.dumps(x) + "\n" for x in kept))
        funnel["sources"][name] = {"scanned": stats["scanned"], "relevant": len(kept)}
        log(f"  {name}: scanned {stats['scanned']}, kept {len(kept)}")

    for name, scanner in socials.items():
        if only and name not in only:
            continue
        log(f"[{name}]")
        stats = {"scanned": 0}
        posts = list(scanner(stats))
        (out / "raw" / f"{name}.jsonl").write_text("".join(json.dumps(x) + "\n" for x in posts))
        funnel["sources"][name] = {"scanned": stats["scanned"], "relevant": len(posts)}
        log(f"  {name}: scanned {stats['scanned']}, kept {len(posts)}")

    # Merge everything on disk for this window, so partial runs (--only) accumulate.
    merged = {}
    for name in scanners:
        p = out / "raw" / f"{name}.jsonl"
        for line in p.read_text().splitlines() if p.exists() else []:
            it = json.loads(line)
            k = key(it["url"], it["title"])
            if k in merged:
                m = merged[k]
                m["found_via"] = sorted(set(m["found_via"]) | set(it["found_via"]))
                m["relevance"] = max(m["relevance"], it["relevance"])
                m["beat"] = m["beat"] or it["beat"]
                m["signals"].update(it["signals"])
            else:
                merged[k] = it | {"id": k}
    for name in socials:
        p = out / "raw" / f"{name}.jsonl"
        for line in p.read_text().splitlines() if p.exists() else []:
            post = json.loads(line)
            for link in post["links"]:
                k = key(link)
                if k not in merged:
                    if rel.score(f"{post.get('title', '')} {post.get('text', '')}") < threshold:
                        continue
                    merged[k] = item(post["network"], type="link", title=post.get("title") or post["text"][:120],
                                     date=post["date"], url=link, abstract=post.get("text", "")) | {
                                         "id": k, "relevance": threshold, "needs_resolution": True}
                merged[k]["signals"].setdefault("social", []).append(
                    {k2: post[k2] for k2 in ("network", "url", "author", "likes", "reposts", "points", "comments")
                     if k2 in post})

    def rank(it):
        s = it["signals"]
        buzz = sum(p.get("points", 0) + p.get("likes", 0) for p in s.get("social", []))
        buzz += s.get("github_stars", 0) / 5 + s.get("hf_likes", 0)
        return it["relevance"] + 1.5 * (len(it["found_via"]) - 1) + 2 * math.log10(1 + buzz)

    ranked = sorted(merged.values(), key=rank, reverse=True)
    for it in ranked:
        it["score"] = round(rank(it), 2)
    (out / "candidates.jsonl").write_text("".join(json.dumps(x) + "\n" for x in ranked))
    # Two reading lists. Life sciences, chemistry and medicine go to a separate drafting pass,
    # so anything in those topics, from a biology server, or matching the screen is kept out of the core list.
    screen = [t.lower() for t in cfg.get("bio_screen", [])]

    def is_bio(it):
        text = f"{it['title']} {it['abstract']}".lower()
        return (it["beat"] in ("life-sciences", "chemistry-medicine") or it["source"] in ("biorxiv", "medrxiv")
                or any(t in text for t in screen))

    bio = [x for x in ranked if is_bio(x)]
    core = [x for x in ranked if not is_bio(x)]
    (out / "candidates.bio.jsonl").write_text("".join(json.dumps(x) + "\n" for x in bio))
    (out / "candidates.core.jsonl").write_text("".join(json.dumps(x) + "\n" for x in core))
    funnel |= {"window": {"since": since.isoformat(), "until": until.isoformat()},
               "generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
               "scanned": sum(s["scanned"] for s in funnel["sources"].values()),
               "relevant": sum(s["relevant"] for s in funnel["sources"].values()),
               "candidates": len(ranked)}
    (out / "funnel.json").write_text(json.dumps(funnel, indent=1))
    log(f"Done: {funnel['scanned']} scanned, {funnel['relevant']} relevant, {len(ranked)} unique candidates "
        f"({len(core)} core, {len(bio)} life sciences)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan")
    s.add_argument("--since")
    s.add_argument("--until")
    s.add_argument("--days", type=int, default=7)
    s.add_argument("--label", help="folder name under data/candidates/")
    s.add_argument("--only", help="comma-separated source names")
    c = sub.add_parser("counts")
    c.add_argument("--from", dest="first", default="2023-01")
    args = ap.parse_args()
    if args.cmd == "scan":
        run_scan(args)
    else:
        cfg = yaml.safe_load((ROOT / "monitor" / "sources.yaml").read_text())
        out = ROOT / "data" / "charts" / "arxiv-volume.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        arxiv_counts(cfg["arxiv"], args.first, out)


if __name__ == "__main__":
    main()
