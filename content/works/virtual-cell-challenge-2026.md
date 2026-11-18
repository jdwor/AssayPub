---
short: "Arc contest: unseen cell responses"
title: 'The 2026 Virtual Cell Challenge: predicting perturbation responses in cell contexts a model has
  never seen'
authors:
- Arc Institute
org: Arc Institute, with NVIDIA, 10x Genomics and Ultima Genomics
date: 2026-08-20
type: benchmark
url: https://arcinstitute.org/news/virtual-cell-challenge-2026
links:
- kind: context
  label: 'Arc Institute: the Virtual Cell Initiative behind the challenge'
  url: https://arcinstitute.org/virtual-cell-initiative
license: ''
beat: life-sciences
edition: '002'
drafted_by: Claude Opus 5
well: C5
tier: notice
importance: Notable
novelty: New program
evidence_type: A competition whose ground truth is new Perturb-seq data generated and withheld by the
  organizers; no entrant results existed at release
evidence: Not applicable
independence: Not applicable
read: partial
read_gap: The challenge website (virtualcellchallenge.org), which holds the rules, the submission format
  and the scoring methodology, needs JavaScript and returned no text to a plain request. Only the announcement
  was read, and the six final metrics are therefore named here only as the announcement describes them.
checked:
- Announcement read in full
- The August 20, 2026 date, the task definition, the timeline and the prize amounts taken from the announcement
- Quotations checked against it
- The challenge website could not be read (see the read gap); the 2025 dataset and the winning team's
  preprint were not opened
- No errors found in the announcement
coi: Arc Institute sets the task and holds the answers while also releasing its own perturbation-prediction
  models, State and Stack. The drafting model is made by Anthropic, which does not participate.
found_via: Web search. The monitor does not follow the Arc Institute news feed.
standfirst: Last year's challenge asked models to generalize to new perturbations inside one cell type.
  This year there is no training set. Entrants see six cell lines only in their unperturbed state,
  plus a list of genes to knock down, and must predict the expression profiles Arc measured and withheld.
---

The 2026 Virtual Cell Challenge asks for predictions of CRISPR-interference knockdown responses in six cell lines that no model has seen perturbed. Entrants receive, for each line, expression profiles from cells carrying non-targeting guides (the basal state of the context) and the identifiers of the genes to be knocked down. They return the post-perturbation profiles that would be measured after knockdown and 10x Flex profiling. Arc generated the data by Perturb-seq across six lines from different tissues of origin sequenced on Ultima's UG100, and withheld the measurements as ground truth. Three lines support the validation phase and a live leaderboard; three are held back to decide winners. Any modeling strategy and any outside training data are allowed; the restriction is on the challenge data alone, which is what makes the task zero-shot.

The 2025 edition supplied H1 embryonic stem cell data and held out perturbations within that same context. This year the held-out axis is the cell type. The announcement gives the reason: "Many of the cellular contexts we care about in human biology are difficult or impossible to perturb directly: rare cell types, primary cells that do not expand outside the body, diseased cells that cannot be cultured faithfully, and tissue states that depend on their native microenvironment."

Scoring changed as well: final rankings now aggregate six metrics, because, the announcement says, "a scoring function with a narrow surface invites optimization against the metric rather than the biology". The evaluation tool, cell-eval, was revised with NVIDIA, which also sponsors the challenge along with 10x Genomics and Ultima Genomics. The grand prize is $100,000, with $50,000 and $25,000 for second and third, paid partly in NVIDIA compute credits. Validation data and the leaderboard opened on August 20, the final test set was due for release on October 22, final submissions on November 5, and winners in mid-to-late November.

The first edition drew more than 5,000 registrations from 114 countries and more than 1,200 teams submitting, of which more than 300 made a final submission; that dataset, including the held-out test perturbations, is now downloadable. Arc writes: "That is the AlphaFold and ImageNet moment we are aiming at for cellular modeling. While we would be pleasantly surprised if anyone reaches this level in 2026, we believe the only way to establish how far away it is, is to measure it in public."

The institute that sets the task and holds the answers also builds perturbation-prediction models, so the challenge is run by an interested party, as last year's was. The task is also still a single assay: knockdown followed by expression profiling in cultured lines. A model that predicts those profiles well in an unseen line has demonstrated transfer across cellular contexts. What a perturbation does to a cell is more than that assay measures. {{aintibody-blinded-benchmark}} measured designed antibodies against an external standard; this challenge builds the equivalent standard for perturbation prediction.
