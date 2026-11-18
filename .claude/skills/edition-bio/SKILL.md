---
name: edition-bio
description: Draft the life-sciences pass of an Assay edition (rows C and D, life sciences and chemistry & medicine) after the main pass has finished. Use when invoked as /edition-bio with a start date, end date and edition number.
---

Draft rows C and D of one edition of Assay. Your work is written directly into the edition and read by the editor. No other model reviews it, so accuracy and verification are entirely on you.

Arguments: start date, end date, edition number (for example `2026-11-01 2026-11-30 005`).

1. Read `StyleGuide.md`, then `editorial/PROTOCOL.md` (the Rules, the Writing section, Stages 3 to 5 and Stage 7), then `content/pages/method.md`.
2. Read the main pass's work as your benchmark for how selective to be and how to write: the assessments in `content/works/` with this edition number, and the `shortlist` in `content/editions/<NNN>.yaml`.
3. Row C is `life-sciences` (AI for biology, including biological datasets, models and tools). Row D is `chemistry-medicine` (chemistry, drug discovery and development, clinical and medical research). Only work first released inside the window qualifies.
4. Browse candidates with `uv run monitor/list.py data/candidates/<start>_<end>/candidates.bio.jsonl` (use `--grep`, `--offset`, `--show`). Search the web, about thirty searches at most, for lab and company posts, widely discussed work, and credible critiques.
5. Shortlist up to twelve items per row. Select what merits it; a row with no selection is acceptable. Prefer work validated in the laboratory, prospectively, or clinically over benchmark gains.
6. Write, and write only:
   - `content/works/<slug>.md` for each selected work, with `edition: "<NNN>"`, `well: TBD`, and no `drafted_by` field;
   - `data/runs/<end-date>/bio-shortlist.yaml`: the shortlisted items you did not select, each with `title`, `url`, `org`, `date`, `type`, `beat` and a one-sentence `note`;
   - `data/runs/<end-date>/bio-note.md`: one paragraph of at most 120 words for the editorial, written to stand in its marked place. Cite a selected work after the statement it supports as `({{file-name}})`, and a shortlist entry by its `id`; never write a well code;
   - `content/topics/life-sciences.md` and `content/topics/chemistry-medicine.md`: revise the existing summaries in light of this edition (keep the `updated` date current);
   - `data/runs/<end-date>/bio-report.md`: your report to the editor (Stage 9).
7. Confirm every number and quotation with `uv run editorial/fetch.py <url> --grep <pattern>`. Then run `uv run editorial/check_quotes.py <your slugs>` and fix every failure. Last, run `uv run editorial/style_check.py --bio <NNN>`, reconsider every sentence it lists, and read your text through once more for the patterns in `StyleGuide.md`.

Screen candidates from titles and abstracts. Read in full every work you select, before you write about it (protocol Stage 4): `uv run editorial/fetch.py <url> --max 60000`, continuing with `--offset`. Set `read: full`, or `read: partial` with a `read_gap`, in each assessment.

If the edition file already holds rows C and D entries from an earlier draft of part of the window, carry forward into your shortlist file the ones that still merit a place. Do not edit the edition file or any assessment you did not write. Do not run the site build. End your reply with a receipt only: paths written, counts per row, and whether the quotation check passed. Keep titles and scientific detail out of the reply; they belong in the files.
