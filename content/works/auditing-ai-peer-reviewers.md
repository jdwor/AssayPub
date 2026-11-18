---
short: Auditing AI reviewers
title: 'Auditing AI peer reviewers: a benchmark on real scientific papers'
authors:
- Íñigo Zubeldia
- Boris Bolliet
- Francisco Villaescusa-Navarro
- Pablo Villanueva-Domingo
- Miles Cranmer
org: University of Cambridge, Flatiron Institute and others
date: 2026-11-12
type: benchmark
url: https://arxiv.org/abs/2611.17052
links:
- kind: material
  label: Benchmark and code
  url: https://github.com/inigozubeldia/skepthical-benchmark
license: CC BY 4.0
beat: infrastructure
edition: '005'
well: G1
tier: notice
importance: Notable
novelty: New resource
evidence: Suggestive
evidence_type: 'Benchmark: 357 errors inserted into 30 preprints, twelve reviewing systems, detection judged by
  a panel of language models'
independence: Peer-reviewed
checked:
- Main text read in full
- Appendix F, the human check of the adjudication, and the license notes read; other appendices not read
- The repository was not examined
coi: The authors built Skepthical, one of the systems compared. Claude models, the family of the model that drafted
  this assessment, are among the systems evaluated.
found_via: Returned by the arXiv monitor (science-of-science lens) and by research agent search of code repositories.
standfirst: A benchmark that inserts 357 known errors into 30 arXiv preprints and measures how many each of 12 AI
  reviewing systems detects. With the same prompt, the detection rates of three frontier models differed by about
  50 percentage points. Detection was judged by a panel of language models.
read: full
---

The benchmark takes real preprints, inserts errors at known locations, and measures which of them an AI reviewer reports. The authors used two sets of 15 arXiv preprints: astrophysics papers posted on April 22, 2026 and machine-learning papers posted on July 15, both after the knowledge cutoffs of the models tested. Each paper was reviewed in four versions: a clean copy, used to count false positives, and three copies each carrying one citation, numerical, mathematical and general error at different severities, 357 errors in all. A panel of three language models from different providers decided whether each review had detected each error.

Twelve reviewing systems were tested. Given the same one-sentence prompt, GPT-5.5 detected 60.5% of the astrophysics errors, Claude Opus 4.7 36.7% and Gemini 3.1 Pro 11.9%. A long structured prompt narrowed the gap. Two open-weight reviewers fine-tuned on conference reviews detected under 3%. Flags about mathematics were the least reliable: across the frontier systems, 30% of those raised on clean astrophysics papers and 67% of those raised on clean machine-learning papers were judged false.

The authors also built one of the systems, Skepthical, which had the highest detection rate on astrophysics (70.6%). They note that the comparison is not matched for cost and that, against a shorter structured prompt for GPT-5.5, its margin is not statistically significant.

Detection was judged by language models. One author checked the panel's verdicts for a single paper without seeing them and agreed on 127 of 132. In all five disagreements the panel had credited a detection that the author rejected. The authors also note that inserted errors may differ from the errors that occur naturally in papers. The paper was accepted at NeurIPS 2026.
