---
short: Agent runs cryogenic microscope
title: 'AIMS: an AI experimentalist turns uncertainty into quantum matter discovery'
authors:
- Siyuan Qiu
- Philip D. Suh
- Nhat Huy Tran
- Xirui Wang
- Heonjoon Park
- Kutay Akin
- Kevin K. S. Multani
- Seungwon Jung
- Wenkai Cai
- Xinyu Liu
- León Garcia
- Ziyan Zhu
- Chunjing Jia
- Zhantao Chen
- Zhixun Shen
- Zhurun Ji
org: Stanford University; SLAC National Accelerator Laboratory; MIT
date: 2026-07-17
type: paper
url: https://arxiv.org/abs/2607.16544
links: []
license: arXiv.org perpetual non-exclusive license
beat: autonomous-discovery
edition: '001'
well: A2
tier: notice
importance: Notable
novelty: New capability
evidence: Preliminary
evidence_type: One experimental campaign on one instrument and one device, with human cross-checks at each stage
independence: Self-reported by developer
checked:
- Main text read in full
- Quotations checked against the source
- No errors found
found_via: Research agent search.
standfirst: A language-model agent operated a cryogenic microwave microscope on a twisted two-dimensional semiconductor.
  It found the sample after cooldown, chose where to measure, and ranked explanations for an unexpected result, asking
  for a calculation and a second measurement to decide between them. The demonstration is one instrument and one
  device, with researchers supplying the question and the starting hypotheses.
coi: The authors built the agent and ran the experiment. The agent runs on Claude Opus 4.5, made by Anthropic, which
  also makes the model that drafted this assessment.
read: partial
read_gap: The methods section and the supplementary information, which holds the table of human interventions, were not
  read.
---

Microwave impedance microscopy maps the local electrical response of a material with a scanning tip, here at a few kelvin. The experiments are slow and uncertain in ordinary ways: cooling shifts the tip by hundreds of microns, the interesting electronic states occupy small patches of a disordered sample, and good data may fit more than one explanation. The Stanford and MIT group behind this paper built an agent, AIMS, on Claude Opus 4.5 with instrument control exposed as tools, and organized it as three loops matched to those three problems.

In the first loop the agent scans, estimates where the tip is from patterned markers, moves and scans again. In tests it reached the target in six scans, and when debris spoiled an image it flagged its own position estimate as unreliable and reconstructed the image before continuing. The authors report that navigation took about 4 hours with the agent against about 10 with scripted control by a person. In the second loop, on a twisted bilayer of molybdenum diselenide, the agent narrowed a large scan to a grid of points, mapped the variation in twist angle and ranked the points by the quality of their signal. A separate, denser survey by researchers picked a spot about 200 nanometers from the agent's.

In the third loop the agent interprets results. Temperature scans showed that of three charge-ordered states, "the half-filled stripe that classical theory predicts should melt first survived longest". Researchers gave the agent two hypotheses, classical and quantum. It added others and found that a classical simulation predicted the wrong ordering and a quantum mean-field model the right one. It then asked for a more exact calculation and for an atomic-force measurement registered to its own maps, to test whether twist disorder explained the result. The calculation supported the quantum account and the measurement ruled out the structural one. In a blind comparison, "independent condensed-matter physicists scored the resulting AIMS reports comparably to the strongest human analyses".

The division of work is stated in the paper: "Researchers provide the guiding question, initial hypotheses, and experimental safeguards, while AIMS expands the hypothesis space, ranks competing mechanisms, specifies follow-up tests, and updates the physical attribution." The follow-up calculation and measurement were carried out by people at the agent's request. The paper adds: "Full autonomy is not, by itself, the relevant benchmark for a cryogenic experiment".

The authors write that "The demonstration of AIMS centers on a single cryogenic instrument and material system." The search covered position and left gate voltage, magnetic field and temperature unexplored, and "the current discovery loop still depends on curated tools, literature, and human-seeded questions, and the mechanism attribution remains probabilistic and evidence-ranked, not a final microscopic theory". The physical finding, that electron hopping stabilizes the half-filled state, rests on this one device and has not been reviewed.
