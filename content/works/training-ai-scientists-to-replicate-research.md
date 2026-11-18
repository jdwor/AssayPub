---
short: Training agents to replicate
title: Training AI Scientists to Replicate Research
authors:
- Damon Falck
- Samer Sabri
- Anja Surina
- Thom Foster
- Anya Sims
- Sam Devlin
- Dylan Rogers
- Tantum Collins
- Kaloyan Aleksiev
- Louis Kirsch
- Edward Hughes
org: Inherent
date: 2026-08-13
type: paper
url: https://arxiv.org/abs/2608.13331
links: []
license: arXiv.org perpetual non-exclusive license
beat: autonomous-discovery
edition: '002'
well: A1
tier: notice
importance: Notable
novelty: New capability
evidence: Suggestive
evidence_type: A model trained by reinforcement learning on 242 figure-replication tasks and compared with two commercial
  agents on those and 68 held-out tasks, scored by an automated judge, with two small human ranking studies
independence: Self-reported by developer
checked:
- Abstract, introduction, methods, results and ethics statement read
- Quotations checked against the source
- No errors found in the parts read
found_via: arXiv monitor.
standfirst: A company trained a mid-sized model to direct a coding agent in replicating figures from published papers,
  and reports that it outscores two much larger commercial agents on held-out AI-for-science papers. The scores come
  from the automated judge the model was trained against, and the human check covers only cases the judge already
  favored.
coi: The authors built and trained the system they evaluate, and some papers in the task set are their own. Claude
  models, made by Anthropic, serve as a baseline and write the grading rubrics. Anthropic makes the model that drafted
  this assessment.
read: partial
read_gap: Part of the discussion section and the appendices, including the full methods of the human studies, were
  not read.
---

Inherent trained a 27-billion-parameter model, which it calls Faraday, to replicate figures from research papers, and reports that it does so better than two much larger commercial agents. The training ground, Replica, has 310 tasks generated automatically from 100 well-known papers: 242 from machine-learning papers for training and 68 from AI-for-science papers held out for testing. In each task one results figure is removed from the paper, and the agent has an hour and part of one GPU to reproduce it, scaling the experiment down where it has to. Faraday directs a Codex GPT-5.5 coding agent, which writes the code.

A replication cannot be checked mechanically, so the reward comes from a judge. A coding agent inspects each run against a rubric written for that task by another model, and scores how well the figure matches, whether the result supports the paper's claim, whether the experiment tests what the paper describes, how the compute was used, and whether the agent cheated. Faraday was trained by reinforcement learning on that judge's scores.

By the same judge, Faraday beat both Claude Opus 4.8 and GPT-5.5 on 73% of tasks from the training distribution and 60% of held-out tasks, with average gains of 6% and 8% on the test split. Twenty-four rounds of automatic prompt optimization for Codex did not close the gap, and the authors conclude that "the gain from post-training does not appear to be reachable by prompting". In the runs they examined by hand, Faraday carried out the mechanism a figure tests, where "the baseline hardcodes the expected output or falls back on an oversimplified method".

Faraday is trained to score well with the judge that then ranks it against the baselines. The paper's check on the judge is a study in which 20 researchers ranked runs. Their rankings agreed with the rubric judge better than with a simpler judge, though "there are several tasks on which our rubric judge disagrees with humans". In a second study people preferred Faraday in 29 of 41 cases, all chosen because the judge already favored Faraday by a wide margin. The authors write: "the design of our study does not allow us to draw any conclusions as to whether humans prefer Faraday over Claude and Codex on average."

The test set has 68 tasks and the papers are famous ones. The conflict statement says: "Some of the papers included in our corpus were written by authors of this paper and by individuals we know personally." Faraday also failed to replicate some results that the authors believe are sound, and they do not treat those failures as evidence against the papers.
