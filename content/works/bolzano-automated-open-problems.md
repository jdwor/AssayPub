---
short: Bolzano at scale
title: 'Bolzano: From Expert-Guided Proof Search to Automated Open-Problem Solving'
authors:
- Adrián Zámečník
- Matěj Kripner
- Martin Koutecký
- Martin Balko
- Jan Grebík
- Pavel Hubáček
- Robert Šámal
- Václav Rozhoň
org: Charles University
date: 2026-10-07
type: paper
url: https://arxiv.org/abs/2610.09769
links:
- kind: material
  label: The Bolzano system
  url: https://bolzano.app/
- kind: material
  label: 'The earlier report: eight results obtained with expert guidance'
  url: https://arxiv.org/abs/2604.16989
license: CC BY-SA 4.0
beat: mathematics-theory
edition: '004'
well: B4
tier: notice
importance: Notable
novelty: New capability
evidence: Preliminary
evidence_type: Unattended runs of a proof-search system on about 3,800 extracted open problems, with four results
  confirmed by the authors of the source papers and the rest counted by estimate
independence: Self-reported by developer
checked:
- Paper read in full
- Quotations checked against the source
- No errors found
found_via: arXiv monitor.
standfirst: A group at Charles University ran its proof-search system without human guidance on about 3,800 open
  problems taken from recent papers, and counts about 200 as solved. Four of those, from papers accepted to STOC
  2026, were confirmed by the papers' authors. The rest of the count is an estimate.
coi: The authors built the system they evaluate. It runs OpenAI models, and the model that drafted this assessment
  is made by Anthropic, a competitor of OpenAI.
read: full
---

Bolzano is an open-source system that runs language models in rounds. Prover agents propose arguments in parallel, a verifier agent criticizes them and updates three shared documents of notes, candidate proofs and results, and a summarizer records the round for the next one. In the experiments reported here the agents worked "without web search, code execution, direct filesystem access, or any tools".

An earlier report from the same group described eight results obtained with some expert guidance. This paper removes the guidance. A separate agent workflow extracted about 3,800 open problems from four sets of papers: new arXiv preprints in combinatorics and algorithms (1,600 problems), papers accepted to STOC 2026 (420), earlier FOCS, SODA and STOC papers (900), and work associated with a combinatorics workshop (880). Each problem received one run of two or four rounds with GPT-5.5 or GPT-5.6 Sol. The system flagged 485 outputs as candidate resolutions, and the authors count 214 as solved.

Most of that count is estimated. A note to the results table says, "Except for STOC 2026, the solved counts are estimates", and that the estimates are "partially informed by LLM-based assessments of whether the output addresses the source question and whether its argument is substantially correct". The four STOC results are the ones the authors checked closely and the source papers' authors confirmed: a low-memory algorithm for detecting planted bicliques, an exponential separation between two kinds of monotone programs, a convex quartic feasibility problem whose only solution is irrational, and a circuit-depth lower bound for a family of quantum states. For two of the four, "the authors reviewed only the main idea, not the full proof".

The authors write that "The verifier is another LLM, not a formal proof checker" and that "Outputs not flagged as promising were not systematically reviewed." Failures found in review "include missing assumptions, proofs addressing weaker versions of the original questions, invalid arguments and rediscoveries of known results". The four experiments used different models and budgets and "include no comparison with direct use of the underlying models", so the paper does not show what the system adds to the models it calls. The authors say that what remains slow is "assessing the correctness, intended scope, and novelty of candidate results".
