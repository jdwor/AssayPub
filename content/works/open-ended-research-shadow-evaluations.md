---
short: "Shadow evaluations"
title: Can AI agents conduct open-ended AI research? Early evidence from two case studies
authors:
- Peter Kirgis
- Sayash Kapoor
- Andrew Schwartz
- Stephan Rabanser
- David Africa
- Konstantinos Voudouris
- Viet Nguyen
- Toby Pilditch
- Magda Dubois
- Harry Coppock
- Cozmin Ududec
- Nitya Nadgir
- Matilda Orona
- Tilman Bayer
- Derrick Chan-Sew
- Yue Ling
- Abhishek Shetty
- Helen Toner
- Gillian Hadfield
- Seth Lazar
- Steve Newman
- Shoshannah Tekofsky
- Rishi Bommasani
- Arvind Narayanan
author_count: 24
org: Princeton University, the UK AI Security Institute, the University of Toronto and others
date: 2026-07-29
type: paper
url: https://arxiv.org/abs/2607.27191
license: arXiv non-exclusive license
beat: autonomous-discovery
edition: '001'
well: A3
tier: notice
importance: Notable
novelty: New evidence
evidence: Preliminary
evidence_type: 'Expert-graded case studies: two research questions, five agent runs'
independence: Independent
checked:
- Main text read in full; appendices not read
- Quotation checked against the source
coi: The main runs used Claude Opus 4.8, and the drafting model is also a Claude model.
found_via: Research agent search. The arXiv monitor's lenses missed it.
standfirst: The authors gave AI agents the research questions behind two unpublished NeurIPS submissions and asked
  the papers' own authors to grade the results. The agents completed the engineering but made little progress on
  the questions, and both outputs were rejected.
read: full
---

The study introduces what it calls shadow evaluations. An agent receives the central research question of a paper that is not yet public, so the answer cannot be in its training data or on the web, and the paper's authors grade the result as they would a conference submission. The two papers were NeurIPS 2026 submissions, one on the structure of language-model personas and one on detecting distribution shift in tabular foundation models. Each agent, Claude Opus 4.8 running on the OpenClaw scaffold, had six days, $3,000 in model credits, GPU time and web access.

The authors scored the agents' papers 2 and 1 on a six-point scale, both rejections. The abstract reports: "The agents completed all of the engineering without human help, yet could not make substantial progress towards answering the research questions." The agents dropped their most ambitious hypotheses within the first ten hours on the basis of small experiments, did not change approach when their own AI reviewers kept returning rejections, and finished with more than half of their model budget unspent. The authors found no evidence that the agents misrepresented results. A repeat of one task with GPT-5.6 Sol and a different scaffold failed in similar ways.

The evidence is two papers and five runs, and the graders knew the work was written by AI and are coauthors of this study. The authors state these limits and add that some of them are publicly skeptical of near-term recursive self-improvement, which could affect how they designed and interpreted the study. The tasks were machine-learning research, so the result applies to other sciences only by analogy. The expert reviews are public, along with the agent logs for one of the two papers.
