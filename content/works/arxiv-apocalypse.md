---
short: arXiv surge
title: Is the arXiv Apocalypse upon us? A break in preprint growth coincident with agentic AI
authors:
- Carlo R. Contaldi
org: Imperial College London
date: 2026-10-25
type: paper
url: https://arxiv.org/abs/2610.34449
links:
- kind: context
  label: arXiv's announcement of its submission limit
  url: https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/
  date: '2026-10-01'
license: CC BY 4.0
beat: science-of-science
edition: '004'
well: F3
tier: lead
importance: Notable
novelty: New evidence
evidence: Suggestive
evidence_type: Interrupted time-series on three decades of arXiv submission counts and metadata
independence: Independent
checked:
- Paper read in full
- arXiv's announcement of the submission limit read
- Quotations checked against the source
found_via: Research agent search. The arXiv monitor's lenses missed it.
standfirst: An analysis of thirty years of arXiv submission counts finds that submissions outside computer science
  have run 17% above trend since December 2025, with the largest increase in mathematics. The paper attributes the
  change to agentic AI on the basis of timing.
coi: The paper's analysis and first draft were produced with Claude Opus 5.5. Anthropic makes that model and the
  model that drafted this assessment.
read: full
claims:
- claim: arXiv submissions without a computer-science listing have run 17% above their long-run trend since a break
    between December 2025 and February 2026.
  status: supported
  note: From a trend with seasonal terms fitted to three decades of monthly counts. The field-level trends are fitted
    to less than four years of data.
- claim: The break is caused by agentic AI.
  status: unverified
  note: The attribution rests on timing. The author writes that an unrelated change affecting formal fields from
    early 2026 would look the same.
- claim: Mathematics shows the largest excess, and 67% of its growth comes from a larger number of distinct authors.
  status: supported
  note: From submission metadata. The data and code are available from the author on request.
- claim: arXiv's limit of two new submissions a month per submitter produced no visible reduction in volume in its
    first three weeks.
  status: supported
  note: Based on a count for October taken on October 23.
---

The paper fits a trend with seasonal terms to monthly arXiv submissions, which "have grown exponentially for three decades, at about 9% per year". It finds a break in the growth rate "between December 2025 and February 2026" that "is absent from the AI categories themselves". Since then "submissions without a CS listing have run 17% above trend", and September 2026 had a record 40,363 submissions. The earlier acceleration, from 2022, was confined to computer science. Outside it, growth from 2022 to 2025 stayed at 8% a year.

Mathematics shows the largest excess. It received 3,945 submissions without a computer-science listing in September 2025 and 8,203 in September 2026. The author attributes 67% of that growth to a larger number of distinct authors, 18% to more papers per author and 15% to smaller author teams. The paper reports that "solo-authored papers rose by 70% within a year in mathematics and condensed matter" but not in experimental particle physics, which serves as the control. Theoretical fields show larger excesses than experimental ones.

On October 1, arXiv limited each submitter to two new submissions a month ({{fair-moderation-equitable-access-and-ai}}). The paper's count for October, taken on October 23, was already above the total for October 2025, and the author concludes that the limit "has produced no visible reduction in volume in its first three weeks".

The analysis uses submission counts and metadata and does not use AI-text detectors. As the author writes, it "cannot identify which papers were produced with them or assess their quality", and "an unrelated change affecting formal fields from early 2026 would produce a similar signature". The field-level trends are fitted to less than four years of data. In experimental particle physics the excess over trend is about as large as in theoretical particle physics, and the author calls that comparison "inconclusive" on this measure. The data and code are available from the author on request.

The paper has a single author, Carlo Contaldi of Imperial College London, and has been submitted to a journal. Contaldi states that data collection, analysis and the first draft "were carried out with Claude Opus 5.5 (Anthropic), operating as an agent" under his direction, in about 3.75 hours.
