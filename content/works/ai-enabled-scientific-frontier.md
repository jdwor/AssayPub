---
short: AI vs. older methods
title: The AI-Enabled Scientific Frontier
authors:
- Gabriel Manso
- Emma Fu
- Neil Thompson
org: MIT FutureTech
date: 2026-09-14
type: paper
url: https://arxiv.org/abs/2609.16258
license: CC BY 4.0
beat: science-of-science
edition: '003'
well: F3
tier: notice
importance: Notable
novelty: Synthesis
evidence: Suggestive
evidence_type: A corpus of 2,507 published head-to-head method comparisons drawn from 268 papers
independence: Independent
checked:
- Main text read in full; supplementary sections consulted for corpus construction and bias checks
- Quotations checked against the source
coi: Neil Thompson is also a co-author of Google's study of AI in science ({{ai-in-science-early-insights}}). The
  work was funded by Open Philanthropy.
found_via: Research agent search. The arXiv monitor's lenses missed it.
standfirst: An analysis of 2,507 published comparisons between AI methods and the techniques they replace. Against
  traditional statistics, AI was more accurate but more computationally costly in 59.6% of cases and worse on both
  measures in 23.6%.
read: full
---

The authors collected 2,507 comparisons from 268 papers, published between 2000 and early 2025 across 27 disciplines, in which an AI method and another analysis technique were evaluated on the same task and both performance and computational cost were reported. They sorted the other techniques into traditional statistics, such as random forests and logistic regression, and scientific computing, such as numerical solvers and simulations.

Where AI replaced traditional statistics, "in 59.6% of comparisons, AI performs better but at higher computational cost. Another 13.9% are win-win", and "Lose-lose cases occur in 23.6% of comparisons". The lose-lose share has stayed near 22% since 2016. Where AI replaced scientific computing, "AI is win-win (better performance, lower cost) for 41.1% of comparisons and efficiency-prioritizing for 44.8%." The win-win share against scientific computing rose from 30.5% in 2016–2019 to 49.5% in 2020–2024. Results vary by field: AI was better on both measures in 38.3% of comparisons in earth and space sciences and 8.0% in the life sciences.

The authors note that "Only about half of the comparisons in our dataset report numerical cost metrics" and that the papers come mostly from research communities with established benchmarking practices. The study measures predictive performance and computing cost and does not address interpretability or robustness.

The comparisons average about nine per paper, so they are not independent observations. The extraction records a "proposed" method and a baseline for each one, which indicates that many comparisons come from papers introducing the AI method. The main text does not discuss how far that favors AI. The authors say the dataset and code are in a GitHub repository.
