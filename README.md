# Assay

A pilot of journal-free curation for AI in science. Each edition scans open sources, places up to 80 works on a plate (eight topics, ten wells each; `wells_per_row` in `site.yaml`), selects about fifteen, and publishes an assessment of each. "Assay" is a working title; change it in `site.yaml`.

Purpose and policies: `content/pages/charter.md`. Public method: `content/pages/method.md`. Operating procedure: `editorial/PROTOCOL.md`. Prose rules: `StyleGuide.md`.

## See the site

    uv run site/build.py --serve

Then open http://localhost:8017. The built site is in `dist/` as static files; only this public build writes there. `--drafts` builds the editor's preview, with unsigned drafts, into `preview/`. Feeds need the site's full address: the publishing workflow supplies it, and `url` in `site.yaml` sets it for any other deployment. Everything runs through [uv](https://docs.astral.sh/uv/), which fetches each script's dependencies on first use.

The site follows mockup A3 ("Matrix"): the home page is the edition's cover, which prints the plate with each topic's selections beside its row. Each edition takes one cover color, set as `cover` in its file or assigned in turn by the build. The design rules are in `.impeccable.md`.

## Layout

| Path | Contents |
|---|---|
| `site.yaml` | Name, tagline, editor, public address |
| `StyleGuide.md` | The editor's prose rules; every drafting pass follows them |
| `content/beats.yaml` | The eight topics (plate rows, topic pages) |
| `content/editions/` | One file per edition: subject, editorial, funnel, shortlist, follow-ups |
| `content/works/` | One file per selected work: the assessment |
| `content/topics/`, `content/pages/` | Topic summaries; charter, method, corrections |
| `monitor/` | The scanner, its source list, and a candidate browser |
| `editorial/` | Protocol, quotation checker, source reader, well assignment, signing |
| `site/` | Build script, templates, styles, fonts |
| `scripts/` | The monthly run, its scheduler, and the cover checks |
| `data/charts/` | Monthly arXiv counts for the topic charts |
| `.github/workflows/pages.yml` | Builds and publishes the site on GitHub Pages |
| `.impeccable.md` | Design rules |

## The monthly cycle

`scripts/monthly.sh` does steps 1 to 4. Editions cover calendar months; `editorial/next_window.py` says which month is due.

1. **Scan.** `uv run monitor/scan.py scan --since <start> --until <end>` writes ranked candidates to `data/candidates/<window>/`, split into `candidates.core.jsonl` and `candidates.bio.jsonl`.
2. **Main pass.** A headless Claude run (default Claude Fable 5.2) drafts every topic except life sciences and chemistry & medicine.
3. **Life-sciences pass.** A second run (default Claude Opus 5) drafts rows C and D, using the main pass as its benchmark. Its text goes directly into the edition; the main model does not read it.
4. **Merge and check.** `editorial/assign_wells.py` merges the two passes and numbers the wells. `editorial/check_quotes.py` checks every quotation against its source. `site/build.py --drafts` builds a preview into `preview/`.
5. **Review.** Read the reports in `data/runs/<end-date>/` and preview with `uv run site/build.py --drafts --serve`. Drafts never appear in a normal build.
6. **Sign.** `uv run editorial/sign.py <NNN> --editor "Your Name"` makes the edition public (`--dry-run` lists what it would sign). Nothing else does. Then commit and push: the site is rebuilt and published from `main`.

To turn on the schedule: `scripts/schedule.sh install`. It checks at login and at 06:00 each day, or at the next wake, and drafts an edition once a calendar month has ended. `scripts/schedule.sh remove` turns it off; `status` reports.

Settings are environment variables read by `scripts/monthly.sh`: `ASSAY_MODEL`, `ASSAY_BIO_MODEL` (`none` skips the second pass), `ASSAY_BUDGET_USD`, `ASSAY_BIO_BUDGET_USD`.

## Publishing

The repository publishes itself. On every push to `main`, `.github/workflows/pages.yml` runs the public build and deploys `dist/` to GitHub Pages. Set it up once: in the repository's Settings, under Pages, choose "GitHub Actions" as the source. A draft edition is in the repository, where anyone can read its files, but it is not on the site until it is signed.

Some folders are left out of the repository (see `.gitignore`) and exist only on the editor's machine: the monitor's output and its cache of fetched sources (`data/candidates/`, `data/cache/`), run reports (`data/runs/`), the pilot's working files (`data/pilot/`), and earlier designs (`archive/`, `mockups/`).

## Other commands

    uv run monitor/list.py <candidates file> --grep "pattern"   # browse candidates
    uv run editorial/fetch.py <url> --grep "pattern"            # read a source as exact text
    uv run editorial/check_quotes.py --edition 000              # check quotations
    uv run monitor/scan.py counts --from 2023-01                # refresh topic charts (about 25 minutes)

## Adding a work by hand

Copy a file in `content/works/`, edit the front matter, and build. `short` is the label printed on the cover, four words at most. The build stops with a message if a field is missing, a rating term is outside the vocabulary, a well is used twice, or a link has no `kind`.

## Limits

- No human has reviewed the pilot editions. Every assessment is labeled as a draft.
- Claude Fable 5.2 and Claude Opus 5.5 are restricted on some biological content and cannot draft rows C and D. Those rows use Claude Opus 5.
- In the pilot the monitor found 8 of the 18 main-pass selections without web search. Feeds for the sources it missed have been added; track this in each run's report.
- X has no open API. Discussion there is found by web search during drafting.
