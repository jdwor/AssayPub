# Editorial protocol

How a draft edition is made. Editions are monthly. The scheduled run follows this file, and so should a person doing the work by hand. The public description of the same process is `content/pages/method.md`; keep the two consistent.

An edition is drafted in two passes by two models:

- **Main pass** (default model: Claude Fable 5.2). All topics except life sciences and chemistry & medicine.
- **Life-sciences pass** (default model: Claude Opus 5, `claude-opus-5`). Rows C and D only. It runs last, uses the main pass's shortlist and assessments as its benchmark for selection and style, and writes its content directly into the edition. The main-pass model does not read or review it, because that model is restricted on some biological content.

After both passes, scripts assign wells, check quotations and build a preview. An editor reviews and signs.

## Rules

1. **The run does not publish.** It writes a draft edition (`status: draft`) and stops. Only `editorial/sign.py`, run by the editor, makes an edition public.
2. **Nothing is invented.** A title, author, date, number, quotation or address goes into an assessment only if it was read at the primary source during this run. If a source cannot be opened, say so in the text.
3. **Quotations are exact.** Every passage in quotation marks must pass `editorial/check_quotes.py`. A quotation from a source that could not be opened is attributed in the text to the publication that printed it and is listed under `quotes_unverified`.
4. **Signed editions are not edited.** A change to a signed assessment is a correction and goes on the corrections page. Something that happens to a work after its edition is a follow-up in a later edition (Stage 6), and the earlier assessment stays as it was.
5. **Stay inside the project folder.** No commits, pushes or messages.
6. **Do not work around a safety restriction.** If work on a subject is blocked, record it in the report and continue with the rest.
7. **The main pass leaves rows C and D alone.** It does not read `candidates.bio.jsonl`, does not shortlist or assess work in life sciences or chemistry & medicine, and does not read or edit the files the life-sciences pass writes.

## Writing

Follow `StyleGuide.md` at the project root. In practice:

- State what the work did, what it found and what limits apply, in that order, in plain sentences. Give numbers with their source.
- No section headings inside an assessment. No headings of the form "What it is" or "Why it matters".
- Do not announce importance, count lessons, stage questions, or end on a general moral. Avoid "X, not Y" constructions and paired mirror sentences unless the contrast is the content. Do not swap "X, not Y" for "X rather than Y"; say what is the case.
- Start a paragraph with its first fact. A sentence that only labels what follows ("The paper states its limits.", "The argument is about incentives.", "Three features limit what the numbers show.") is cut, and so is a closing sentence that restates the paragraph. This holds for the editorial too: no slogan openers ("The money kept coming.").
- Introduce a quotation plainly ("Tao writes:") or work it into the sentence. Do not characterize it first ("draws the general point:", "is the method in one sentence:", "ends on a different note:").
- State a limit once. Do not repeat in the body what `coi` says; the conflict note is printed directly under the text.
- No dashes as punctuation outside quotations. No idiom or personification ("did the rest", "cuts against", "vouch").
- Refer to another work or a shortlist entry by token, never by well number: `{{file-name}}` for a selected work, `{{id}}` for a shortlist entry. The build turns the token into the well label and a link, and stops on a token that matches nothing. Wells are renumbered whenever a row changes. Put the token in parentheses after a description ("a Google survey ({{file-name}})"), because it prints as a well label and cannot be the subject or object of a sentence.
- Quote passages of at least a few words. A quoted fragment of one or two words confuses the quotation checker.
- The assessment does not talk about itself. No "we" or "our", and no account of what was searched, read, or could not be opened, why the work was selected, or why it got its rating. Those facts go in the front matter (`read`, `read_gap`, `checked`). The same holds for shortlist notes.
- Do not praise or scold. Words like "candid", "honest", "striking" and "landmark" (outside the rating term) are not needed.
- Do not use templates. Assessments should differ in structure when the works differ.
- American spelling. Dates as "November 16, 2026".
- Quotations keep the source's spelling and punctuation.

When a pass has finished writing, it runs the style check on its own text and reconsiders every sentence listed:

    uv run editorial/style_check.py --main <NNN>     # main pass
    uv run editorial/style_check.py --bio <NNN>      # life-sciences pass

A listed sentence is a prompt for judgment and may stay if the pattern carries the content. The check finds only the patterns it knows, so read the text through once more as an editor would.

## Stage 1. Scan

    uv run monitor/scan.py scan --since <start> --until <end>

The monitor writes `funnel.json`, `candidates.core.jsonl` (for the main pass) and `candidates.bio.jsonl` (for the life-sciences pass) to the folder it reports. Candidates are ranked by a keyword score that exists only to order reading.

## Stage 2. Search for what the monitor cannot see

Search the web, with a limit of about thirty searches, for:

- the sources listed under `web_search_only` in `monitor/sources.yaml`;
- work from the window that researchers discussed widely on X, Bluesky, Hacker News and specialist blogs;
- critiques, corrections, failed replications and retractions of AI-for-science claims;
- funding calls, programs and policy documents announced in the window;
- responses, dated inside the window, to the lead selections of the previous three editions (for follow-ups, Stage 6).

## Stage 3. Shortlist

Sort candidates into the topics in `content/beats.yaml`. A topic's row holds at most ten works, selected and shortlisted together (`wells_per_row` in `site.yaml`). Aim for 20 to 25 shortlisted works in an edition. For every shortlisted item:

- open the primary page and confirm the title, the first-release date and the address;
- confirm it was first released inside the window (for arXiv, the date of version 1);
- confirm it has not appeared in an earlier edition (search `content/editions/` and `content/works/`);
- write one sentence saying what it is.

Engagement is a way to find work and is not a reason to shortlist it.

A funding call, prize or program is a candidate for the institutions row like any other work (`type: rfp`, `prize`, `fellowship` and so on), with its deadline in the note. Editions carry no separate list of open calls.

## Stage 4. Select

A monthly edition usually has about five lead selections and about ten notices across all topics. Fewer is acceptable, and so is a topic with no selection. Criteria, in order:

1. **Importance.** If the claims hold, how much does this change what the field knows or can do?
2. **Credibility.** How well are the claims supported, and by whom? Evidence tested against an external standard counts for more than a demonstration. A developer's report on its own system is eligible and is labeled as such.
3. **Novelty.** What kind of contribution is it?

Work that is important but weakly supported can be selected when readers need to know how far to trust it. The assessment must say the evidence is weak.

**Read what you select.** Scanning and shortlisting can be done from titles and abstracts; there is no need to read every candidate. Once you have chosen the works to highlight, read each one in full before writing about it. An abstract, a summary or another pass's notes do not count. If the full read changes your view, drop the work or change its rating. Read all of the main text, including limitations, funding and conflict statements, and consult appendices where they bear on the claims:

    uv run editorial/fetch.py <url> --max 60000              # then continue with --offset

For a dataset, benchmark or tool, read the paper and the documentation. If part of a selected work cannot be read (a closed journal version, a 166-page proof, a repository of hundreds of manuscripts), keep it only if it matters enough to justify that, and record exactly what was not read.

## Stage 5. Assess

Write one file per selected work in `content/works/<slug>.md`, copying the front matter of an existing file. The build rejects a file with a missing field or a term outside the vocabulary. Leave `well: TBD`; a script assigns wells. Set `short` to the title the cover prints beside the work's well: at most five words, as plain as five words allow. A reader should be able to tell what the work is, so name the subject and, where it fits, the result ("200 open problems claimed solved", "Agents stall on open research"). A little life is fine ("Sixteen agents, one error"); a system's or paper's name alone ("Bolzano at scale"), a quip that needs the article ("Crop the target") and bare jargon ("MXenes") are not.

- **Read the work in full**, for notices as well as lead selections (see Stage 4). Set `read: full`. If part could not be read, set `read: partial` and `read_gap: "<what was not read and why>"`. The build rejects an assessment without these fields. Record what else was checked under `checked`.
- **Describe before judging.** State what the work is and what it claims in terms its authors would accept.
- **Rate in the fixed terms** defined on the method page. When unsure between two terms, choose the more cautious.
- **Main claims (lead selections).** List three to five. Mark each `supported`, `self-reported`, `unverified` or `disputed`, with a note.
- **Concerns.** List one only if it names the passage or claim, can be verified from the source, and would weaken a main claim. State confidence. Report any reply from the authors. For a dispute between others, quote each side exactly and do not say who is right unless the record settles it. Limits that the authors state belong in the body text. If nothing meets the criteria, list no concern and add `No errors found` to `checked`.
- **Conflicts.** Record under `coi` the authors' ties to what they evaluate, and the drafting model's. The drafting models are made by Anthropic; say so when the work is Anthropic's, uses Anthropic's models, or comes from a direct competitor.
- **License.** Record it. The site links to the original and does not reproduce it. Include the abstract only if it is in a public metadata record (arXiv, Crossref).
- **Links.** Each entry under `links` has a `kind`: `material` for the work's own code, data, appendix or other version; `response` for someone else's critique, evaluation, report or commentary, with its `date`; `context` for background. A label says who and what, for example `Kevin Buzzard: what a Lean check establishes`. The page prints each kind under its own heading.
- **Model.** Set `drafted_by` to the name of the model writing the assessment.

## Stage 6. Assemble (main pass)

Write `content/editions/<NNN>.yaml`, copying the structure of the latest edition. If the file already exists as a draft for part of the window, redo it for the whole window: keep the selections and shortlist entries that still merit their place, add the rest, and rewrite the editorial.

- `status: draft`
- `cover`: optional. A flat color for the edition's cover that takes black ink. Leave it out and the build assigns one in turn.
- `title` (the month, as in "October 2026") and a one-sentence `dek`, both plain descriptions;
- `note`: the editorial, 250 to 400 words. It makes an argument about the period from the works: what they add up to, where the evidence is strong or weak, how they bear on one another. It is not a list of items. The first paragraph, at most 65 words, is printed on the cover and must stand alone, so it opens on the facts and does not announce a subject. A month with no single thread opens on its most important development and treats the rest in turn; do not force a theme. It follows the Writing rules: no "we", and nothing about how the edition was made. Put the line `<!-- rows C and D -->` on its own where a paragraph on life sciences and medicine belongs;
- `subject`: the name of the editorial, printed as its heading on the cover and beside the month in the archive. One word where it can be, three at most: a plain noun ("Volume", "Checking", "Jacobian"), never a claim, a question or a headline. For a month without a thread it names the development the editorial opens on;
- `funnel`: from the monitor's `funnel.json`;
- `shortlist`: every shortlisted item that was not selected (`well: TBD`);
- `followups`: optional, and short. An entry reports something that happened inside the window to a work assessed in an earlier edition: a replication, a formal check, a refutation, a correction, a withdrawal. Look among the lead selections of the previous three editions. An entry needs a named party other than the work's authors (or the authors correcting or withdrawing) and a finding a reader can check; commentary alone is not one. No entry is better than a thin one, and an edition carries at most five. Read the source in full first. Each entry has `work` (the earlier assessment's file name), `date`, `by`, `url` and `text`: one to three sentences on what was examined and what was found, under the Writing rules. If the finding changes a rating, add `change`, for example `change: {evidence: Solid}`; the build then shows the new rating on the earlier page with the first one beside it. Do not edit the earlier assessment. Follow-ups on rows C and D are not yet written by either pass.

## Stage 7. Life-sciences pass

Run by the second model after the main pass has finished. It:

1. reads this file, `StyleGuide.md`, the method page, the main pass's assessments in `content/works/` and its shortlist in the edition file, and uses them as the standard for how selective to be and how to write;
2. reads `candidates.bio.jsonl` and does its own Stage 2 search for life sciences, chemistry and medicine;
3. fills rows C and D (at most ten works in each, usually three or four selected between them), following Stages 3 to 5;
4. writes its assessments to `content/works/`, its unselected shortlist to `data/runs/<end-date>/bio-shortlist.yaml`, one paragraph for the editorial to `data/runs/<end-date>/bio-note.md`, written to stand in the editorial's marked place and to carry its argument forward (read the editorial in the edition file first), and topic summaries to `content/topics/life-sciences.md` and `content/topics/chemistry-medicine.md`;
5. runs `uv run editorial/check_quotes.py <its slugs>` and fixes failures, then runs the style check (`--bio`) and revises;
6. writes its own report to `data/runs/<end-date>/bio-report.md`.

## Stage 8. Merge and verify (scripts)

    uv run editorial/assign_wells.py <NNN> --bio data/runs/<end-date>
    uv run editorial/check_quotes.py
    uv run site/build.py --drafts

`assign_wells.py` merges the life-sciences shortlist and editorial paragraph into the edition file and numbers the wells in each row by release date. The preview is built into `preview/`. Only the public build (`uv run site/build.py`, no flag) writes `dist/`, the folder that is deployed.

## Stage 9. Report

Each pass writes a report for the editor in `data/runs/<end-date>/`:

- the funnel in one line;
- each selection with a one-sentence reason, and two or three near-misses with the reason they were not selected;
- items that need the editor's judgment: uncertain ratings, concerns raised, conflicts of interest;
- sources that could not be opened and anything that was blocked;
- how many selections the monitor found without web search, and which feeds or search terms would have found the rest.

To preview: `uv run site/build.py --drafts --serve`. To see what signing would cover: `uv run editorial/sign.py <NNN> --editor "<name>" --dry-run`. To sign: the same without `--dry-run`; it refuses if no assessment names the edition.
