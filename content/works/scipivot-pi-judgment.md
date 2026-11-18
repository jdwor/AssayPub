---
short: Agents miss PI corrections
title: 'SciΠvot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents'
authors:
- Youran Sun
- Xingyu Ren
- Chugang Yi
- Kejia Zhang
- Di Wu
- Yingkang Cao
- Allen Zhou
- Jianping Ye
- Suying Liu
- Jiaxuan Guo
- Jianda Du
- Weicheng Ye
- Kecheng Liu
- Hefan Zhang
- Haixin Wang
- Jie Xiao
- Eric Yang
- Haizhao Yang
org: University of Maryland, College Park; Gradient Network
date: 2026-10-15
type: benchmark
url: https://arxiv.org/abs/2610.21082
links:
- kind: material
  label: The benchmark's questions, reference answers and prompts
  url: https://github.com/AutoResearch-Factory/SciPIvot
license: CC BY 4.0
beat: infrastructure
edition: '004'
well: G2
tier: notice
importance: Notable
novelty: New resource
evidence: Suggestive
evidence_type: Benchmark of 248 two-way choices reconstructed from human corrections in 26 agent-run research projects,
  answered by five models and thirteen researchers
independence: Independent
checked:
- Main text read in full, with the appendices on writer sensitivity, option order and the human baseline
- Quotations checked against the source
found_via: arXiv monitor.
standfirst: A group that ran research agents on 26 projects for six months turned the moments when senior researchers
  corrected the agents into a 248-case test. Shown an agent's plan and the corrected plan, four of five current models
  picked the agent's plan more often. The cases were selected using the same models' answers and were written by
  a model.
coi: The cases come from the authors' own agent-run projects. Claude Opus 5, made by Anthropic, is one of the five
  models tested, and Anthropic makes the model that drafted this assessment.
read: full
---

For about six months a group at the University of Maryland and the company Gradient Network ran language-model agents on 26 research projects in applied mathematics, machine learning, robotics, mechanics, biological imaging and earth science, with publication as the goal. They report: "Keeping experiments running proved easier than choosing experiments that advanced the scientific question." Senior researchers "reviewed projects several times daily to identify stalled or misdirected work and choose the next test".

The benchmark is built from those interventions. Each of its 248 cases gives a model the project's files as they stood before a senior researcher stepped in, with two plans: the one the agent had proposed and the one the researcher's correction led to. Choosing the corrected plan counts as right. The authors sort the corrections by the judgment involved. In 123 cases the agent started costly runs before basic checks or ran experiments too small to answer the question, in 122 it tested a claim other than the project's own, in 88 it overlooked suspicious results, in 65 it kept a hypothesis that earlier experiments had undercut, and in 47 it declared success or failure too early. In one example an agent saw a small model score zero on a coding benchmark and proposed moving to a larger model. The researcher kept the small model, and an audit found that the scoring script had failed to extract the answers.

Five models were tested: GPT-6 Astra, Claude Opus 5, Grok 4.6 and two variants of GPT-5.6. With the project record and medium reasoning effort, four of the five chose the agent's original plan more often than the correction. Accuracy ranged from 29.2% to 59.5%. Thirteen PhD students and postdocs new to the projects, working with an AI assistant, reached 73.4%. Every model did better when shown only the two plans, without the project record: 55.8% on average against 39.2%. The authors' explanation is that the record contains the original agent's mistaken interpretations and the models accept them. Asking a model to reconsider repaired some answers and spoiled others: "the first review repairs 422 errors and introduces 302".

The scores describe a selected set. The authors collected 120 responses per case from the same five models and "retained cases whose model responses vary across the two plans", so that, in their words, "the resulting scores are diagnostic and measure recognition on decisions where models disagree rather than accuracy on research decisions in general". The paper does not say how many candidate cases were dropped. Both plans in each case were written afterward by a model that could see how the project turned out ("Grok 4.6 wrote the cases"), and the check on whether the choice of writer matters covered 13 cases. Models scored above chance with no project record at all, which means the plans carry some signal by themselves. Answers also depended on the order of the two plans. Shown the plans alone, Claude Opus 5 chose the corrected plan 44.0% of the time when it came first and 73.8% when it came second. The researchers who served as the human baseline disagreed with the senior researcher's correction in about a quarter of cases.

The questions and reference answers are public. The project records are to follow, and "Individual model response logs are not part of this release."
