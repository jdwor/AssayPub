---
short: "Virtual cell model ignored drug"
title: 'Discover, Falsify, Revise: Auditing Input-Use Claims from Source Code to Predictive Contribution
  in Agent-Discovered Cell Models'
authors:
- Mengran Li
- Bo Li
- Chengyang Zhang
- Yang Yan
- Jinfeng Xu
- Zhenchao Tang
org: ''
date: 2026-09-23
type: paper
url: https://arxiv.org/abs/2609.27234
links:
- kind: material
  label: 'The authors: the CellAudit project page'
  url: https://limengran98.github.io/CellAudit/
license: CC BY 4.0
beat: life-sciences
edition: '003'
drafted_by: Claude Opus 5
well: C9
tier: notice
importance: Notable
novelty: Audit or replication
evidence_type: Input-replacement tests on frozen checkpoints, with source inspection, on public perturbation
  datasets, reported with paired intervals across seeds and trajectories
evidence: Suggestive
independence: Independent
read: partial
read_gap: Appendices A to O, about 200,000 characters of protocol, statistical and search-trajectory detail
  including the simulated known-truth calibration study and the per-trajectory records, were not read.
  The main text and its tables were read in full.
checked:
- Main text read in full, through the discussion
- Figures quoted here checked against the paper's Table 1 and Section 6
- The version 1 date of September 23, 2026 and the license confirmed on arXiv
- The paper gives no affiliations, funding statement or competing-interest statement, and none was found
- The project page, the appendices and the code were not examined, and no result was recomputed
- No errors found in the main text
coi: The paper audits agentic discovery systems from the recent literature, including CellScientist, which
  it also uses as its search policy. It states no affiliations and no competing interests.
found_via: The arXiv life-sciences lens in the monitor's candidate file.
standfirst: A language-model agent searching for cell-response predictors selected one that scored near
  the top of its task and whose predictions did not move when the compound was replaced. A predictor
  that saw only control wells scored the same.
---

Virtual cell models are meant to predict what an intervention does to a cell. A model can score well on that task while using only the untreated control profile and the systematic structure of the experiment, never the identity of the perturbation. The paper calls the distance between what a model is said to use and what it demonstrably uses the prediction–claim gap, and notes that "held-out predictive performance alone does not establish use of the supplied perturbation information". Its instrument, CellAudit, checks three things about a model whose design claims to use an input: whether the input can reach the computation that is cited for it, whether the fitted model's predictions change when it is replaced, and whether that dependence improves prediction of the measured response. The three can come apart, and most of the paper is about cases where they do.

The main finding comes from a task built on paired cell-imaging and transcriptional profiles, where models predict both readouts from a same-plate control profile, a compound representation and a dose. The agentic search, run under a fixed budget and fixed evaluation folds, selected a model that reached a mean held-out correlation of 0.3153. Replacing the compound with another changed its predictions by exactly zero in every refit; replacing the control profile lowered the correlation by about 0.20. A predictor given only the control profile reached 0.3142, so the model's margin over a baseline that cannot know what was applied is 0.0011, with an interval straddling zero. Source inspection shows the defect: the cited compound-conditioned attention had a single key and value, so its normalized weight is constant and the query cannot carry compound identity. The invariance persisted when the model was refit with input profiles and target references drawn from physically separate control wells, which rules out one way the control profile could have been leaking the answer.

Across a stratified sample of 48 generated candidates on two linked tasks, 47 do change their predictions when the compound is replaced, while only 20 show a gain in target loss whose interval stays above zero on both held-out folds. Source consumption and fitted dependence are, on this evidence, weak proxies for using the perturbation in a way that helps.

Feeding the audit back into the search helps less clearly. On a second dataset, agents given grouped errors, source checks and replacement effects alongside their scores produced models with lower mean error than agents given scores alone, by about 10% and 6% on the two held-out partitions, with larger mean compound and dose contributions; but the paired intervals over five trajectory pairs include zero, which the authors report. A separate repair route, fitting the perturbation branch as a residual over a frozen control-only model, did recover positive compound contributions while keeping a predictive margin, though none of its ten models cleared the paper's reference-relative threshold.

Designs selected on one chemical-perturbation cohort were frozen and refit on a cohort acquired independently. The predictive gains carried over, and so did the contribution of dose. All 50 refits passed the dose criterion at every boundary, and none passed the compound-identity criterion on the new cohort. The authors write that "predictive generalization need not imply generalization of input-use claims".

Replacement tests are conditional on the fitted model, the evaluation setting and the distribution the replacements are drawn from, and the authors add that observed-support replacements "do not establish biological exchangeability, mechanism, or causal effects". The simulated calibration study behind the uncertainty intervals, which the paper says undercovers the population-level effect when only prediction maps are resampled, sits in an appendix. Against the volume of untested predictions in {{alphagenome-atlas}}, this is a cheap test of whether a prediction is about what it says it is about.
