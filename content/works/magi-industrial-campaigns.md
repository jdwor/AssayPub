---
short: "Nine replayed campaigns"
title: 'From Benchmark to Bench: Can Agents Survive Real-World Drug Discovery?'
authors:
- Pierre Llompart
- Levent Guner
- Helen Lai
- Alessandro Tibo
- Yijie Xu
org: AMD Silo AI and AstraZeneca
date: 2026-10-05
type: paper
url: https://arxiv.org/abs/2610.06411
license: CC BY 4.0
beat: chemistry-medicine
edition: '004'
drafted_by: Claude Opus 5
well: D1
tier: notice
importance: Notable
novelty: New evidence
evidence_type: Nine retrospective lead-optimization campaigns from three pharmaceutical companies, replayed
  under fixed temporal cutoffs, with a blinded evaluation by four medicinal chemists
evidence: Suggestive
independence: Self-reported by developer
read: partial
read_gap: Supplementary sections S1 to S5 and S8 (the agent and service descriptions, dataset construction,
  metric definitions and the supplementary figures) were not read. The main text, the medicinal-chemist
  evaluation protocol in S6.3 and the ethics and release notes in S7 were read.
checked:
- Main text read in full, including the limitations
- The chemist-evaluation instrument and its reported outcome checked in the supplementary protocol
- The version 1 date of October 5, 2026 and the license confirmed on arXiv; version 2 was posted on October
  9, 2026
- The nine campaign datasets, the scoring services and the agent's logs were not examined
- No errors found in the main text
coi: Two authors work for AstraZeneca, one of the three companies whose campaigns are replayed and the
  source of the one undisclosed campaign; the other three built the agent they evaluate. The agent runs
  on Claude Sonnet 4.6, and the drafting model here is also Anthropic's.
found_via: The arXiv chemistry lens in the monitor's candidate file.
standfirst: An agent was given nine real lead-optimization projects from GSK, Sanofi and AstraZeneca, each
  replayed as it stood at a fixed date, and asked to write the objective, run the optimization and revise
  its strategy. Whether a campaign reached its goal turned on whether the property predictors were accurate
  on the chemistry the agent proposed.
---

Lead optimization is a loop: propose compounds, predict their properties, make and measure a few, revise. Generative tools such as REINVENT 4 optimize against an objective that a chemist writes and rewrites as evidence accumulates. MAGI is an agent placed one level above that: it authors the objective as a versioned, machine-readable target profile that compiles into a scoring configuration, launches and monitors the optimization, reads the structure–activity relationships that emerge, and revises. It runs on Claude Sonnet 4.6 and reaches 24 tools over a common interface: REINVENT 4, general and project-specific property models, a co-folding model, a pose-validity checker and an interaction profiler. Molecules come either from the language model directly or from REINVENT under the agent's control, with the same objective scoring both.

Nine campaigns were replayed under fixed temporal cutoffs: four published GSK series on a bromodomain target, four Sanofi projects, and one undisclosed AstraZeneca campaign. In each, the agent saw one starting compound and four measured analogues, and everything else, including the compounds the real project went on to make, was withheld from the agent and from the project-specific predictors alike. Five rounds ran per campaign, each ending in an agent-selected shortlist of about five compounds.

Three of the four GSK series and the AstraZeneca campaign met their objectives; of the Sanofi projects, two of four cleared their thresholds, with the language-model route reaching the objective more often than REINVENT while reproducing the quality those programs historically reached. The abstract says: "attainment followed model accuracy on the chemistry proposed, dropping once that chemistry moved outside the model's applicability domain". The two failures are diagnosed in those terms: one series had a solubility target outside the range its scorer was trained on, and one project's ligand-based model correlated weakly on held-out compounds. In the first case the agent noticed and worked around it, promoting a related measurable property as a proxy, after which its proposals improved.

The two routes differed in cost and in behavior. The language model acted as a local optimizer around the chemistry it had been shown, reaching comparable or higher primary activity in fewer operations; REINVENT explored more broadly and required four to nine times as many agent operations for launching, monitoring, recovery and retrieval, on top of exploring 100,000 more structures inside its own loop. Structure-based scoring changed rankings in a target-dependent way: reranking by predicted affinity substantially altered the top five.

A blinded instrument put the output in front of four medicinal chemists: 12 cases asking which of two structures was agent-generated against a similarity-matched withheld compound, 11 asking which candidate to test next among blinded sources, and 5 asking for a verdict on the agent's structure–activity reasoning. "Discrimination accuracy did not separate from chance for any chemist or in pooled analysis, and no source was preferentially selected in the prioritization cases." The reasoning was judged plausible but incomplete. Four participants and 28 questions is a small instrument.

The authors write: "Proposal endpoints are predictions, not measurements." No compound in these campaigns was synthesized; a campaign "met its objective" when the predictors said so, and those predictors fail outside their applicability domain. Each condition used one model backend and one trajectory with no static-objective control, so the agent's contribution is not isolated from the tools it calls, and temporal splits restrict training overlap without excluding what the language model saw during pretraining. Perturbation-response models lost their accuracy outside the distribution they were trained on ({{genetic-perturbation-prediction-models-fail-out}}), and the partner programs in {{anthropic-drug-development}} rest on measurements the companies made themselves. The agent orchestration worked; whether the scorers can be trusted on chemistry that does not yet exist is untested here.
