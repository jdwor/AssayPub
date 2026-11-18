---
title: Method
dek: Sources, selection, rating terms and policies.
---

## 1. Scan

A monitor collects new records from each source for the edition's period. Its code and source list are part of this project.

| Source | Access | Yields |
|---|---|---|
| arXiv | Public API, keyword searches for each topic | Preprints |
| bioRxiv, medRxiv | Public API, all new postings filtered by keyword | Preprints, with license |
| NBER | Working-paper listing | Working papers |
| Laboratory and company sites | Feeds and sitemaps | Technical reports, research posts |
| Newsletters and blogs | Feeds, from a maintained list | Essays |
| Funders | Feeds, grants.gov | Calls, programs |
| Hugging Face, GitHub | Public APIs | Datasets, models, software |
| Bluesky, Hacker News | Public search APIs | Links under discussion, with engagement counts |
| X, and sites with no feed | Web search during drafting | Leads |

Each record is scored by a keyword relevance filter, and duplicates are merged. Each edition reports the number of records scanned, the number passing the filter and the number of unique candidates. Engagement counts are used to find items and are not a selection criterion.

## 2. Shortlist

Candidates are sorted into eight topics. An edition's plate holds up to ten works per topic, 80 in total: about fifteen are selected for assessment and the rest are shortlisted. For each shortlisted item the title, date and address are confirmed at the source, and at least the abstract or opening section is read. An item must have been first released within the edition's period.

## 3. Select and assess

Candidates are screened from titles and abstracts. Every work selected for an edition is then read in full by the model that drafts its assessment. Where part of a work could not be read, such as a closed journal version or a very long proof, the assessment states what was not read and why. Lead selections receive a full assessment and notices a short one.

### Rating terms

**Importance**: how much the work changes what the field knows or can do, if its claims hold.

| Term | Meaning |
|---|---|
| Landmark | Changes the direction of a field. |
| Major | A result or resource that many researchers will need to take into account. |
| Notable | A clear contribution within its area. |
| Useful | Worth knowing about; limited in scope. |

**Contribution**: new capability, new evidence, new resource, new framing, new program, synthesis, or audit or replication.

**Strength of evidence**: how well the main claims are supported.

| Term | Meaning |
|---|---|
| Compelling | Several independent lines of support, or independent replication. |
| Solid | Methods fit the claims, and the stated limitations do not undermine them. |
| Suggestive | The main claim is plausible and partly supported. Alternative explanations or limits on generalization remain. |
| Preliminary | Early evidence: small samples, single cases, demonstrations. |
| Contested | Specific challenges to the main claims, from credible sources, are unresolved. |
| Not applicable | The work makes no empirical claim: a funding call, a program, some essays. |

**Independence**: *self-reported by developer* (the authors built or sell the system the claims concern), *independent*, or *peer-reviewed*.

Each assessment also states any conflicts of interest, says so when part of the work was not read, and shows whether an editor has reviewed it. What was checked for each assessment is recorded in the site's data file.

### Main claims

For lead selections, the work's main claims are listed and each is marked *supported* by evidence in the work, *self-reported* in a way readers cannot check, *not verified* by Assay, or *disputed* by a named source.

## 4. Sign

An editor reads the draft edition against the sources, makes changes, and signs it. Until then every assessment is labeled as not yet reviewed. No edition is published automatically.

## Concerns

A concern about a work is published only if:

1. it names the passage, figure or claim at issue;
2. a reader with the source can verify it;
3. a main claim would be weaker or false if the concern is correct;
4. the confidence in it is stated;
5. any reply from the authors is reported.

For a dispute between third parties, the assessment reports who said what, with exact quotations, and does not say which side is right unless the record settles it.

Authors may reply to any assessment. Replies are published in full below it.

The search for responses to a work is not exhaustive. A page that lists no responses or concerns means that none were found.

## What appears with an assessment

Assay links to the original and does not reproduce it. A page shows the authors' abstract only when the abstract is in a public metadata record such as arXiv or Crossref.

Other links on a page are grouped by what they are: more from the authors (code, data, appendices, other versions), responses and critiques by others, with their dates, and background.

Assay's own text is available under CC BY 4.0.

## Use of AI

The shortlist and assessments are drafted by AI models working from the primary sources: Claude Fable 5.2 for most topics, and Claude Opus 5 for life sciences and for chemistry and medicine, because Fable 5.2 is restricted on some biological content. The two passes are merged by a script, and neither model reviews the other's work. Each assessment names the model that drafted it. Drafts can contain errors such as a misread number or a claim attributed to the wrong section. Quotations in assessments are checked against the source text by a separate program. The editor reads each assessment before signing. Errors found after publication are corrected publicly.

Anthropic, which makes both models, also publishes research in this field. Assessments of work by Anthropic or its competitors carry a conflict notice.

## Follow-ups

A signed assessment is not rewritten when something later happens to the work. If someone other than the authors replicates, formalizes, refutes or corrects a selected work, or the authors withdraw or correct it, the edition for the month in which that happened reports it as a follow-up: who examined what, and what they found. The follow-up is listed at the foot of that edition's editorial and on the page of the earlier assessment. If it changes a rating, the page shows the new rating with the first one beside it.

## Corrections

Errors in assessments are handled separately, on the [corrections page](../corrections/).
