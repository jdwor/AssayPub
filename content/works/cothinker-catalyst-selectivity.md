---
short: "Model steered a CO2 catalyst"
title: Reaction-network reasoning with frontier models for experimentally confirmed catalyst-selectivity
  hypotheses
authors:
- Sutanay Choudhury
- Anwesha Banerjee
- Udishnu Sanyal
- Jorin Dawidowicz
- Chiezugolum Ijeoma Odilinye
- Jesun Firoz
- Liney Arnadottir
- Simone Raugei
- Johannes Lercher
- Arnab Dutta
org: Pacific Northwest National Laboratory, Indian Institute of Technology Bombay, Oregon State University
  and the Technical University of Munich
date: 2026-07-09
type: paper
url: https://arxiv.org/abs/2607.08003
license: CC BY 4.0
beat: chemistry-medicine
edition: '001'
drafted_by: Claude Opus 5
well: D3
tier: notice
importance: Notable
novelty: New evidence
evidence_type: Mechanistic hypotheses fixed before synthesis, then tested by electrochemical measurement
  of four catalyst compositions under varied electrolytes
evidence: Suggestive
independence: Self-reported by developer
read: full
checked:
- Preprint read in full
- Figures and quotations checked against the source text
- License and the version 1 date confirmed on arXiv
- The electrochemical data and the reaction network were not independently checked
- No errors found in the text
coi: The authors built the framework they evaluate.
found_via: Named by the editor and returned by the arXiv monitor (chemistry lens).
standfirst: A language model confined to reasoning over an explicit network of elementary reaction steps
  proposed three controllable variables for steering carbon dioxide reduction toward acetate. The predictions
  were fixed before synthesis; a 1:1 copper-iron oxide then gave about three times the acetate selectivity
  of copper-rich controls.
---

Electrochemical reduction of carbon dioxide can yield several products from shared intermediates, and which one dominates is set at one or two branch points. The authors built a framework, CoThinker, that converts a stated catalytic objective into an explicit directed graph of chemical species and elementary steps, and then requires a reasoning model to work only over that graph, a constraint they call network invariance. The paper's claim is that "frontier language models, when strictly constrained to reason over explicit reaction networks, can discover novel catalysts by identifying the physical levers that govern pathway competition".

The network began with 32 species and 38 elementary transformations and was extended by the model to 41 steps spanning the acetate, ethylene, ethanol, methane and formate pathways. The model ranked five high-leverage control elements and named hydroxide-assisted desorption and capture of ketene as the acetate-forming step, with local hydroxide activity, iron incorporation and the accessibility of interfacial proton donors as the variables to manipulate. It also proposed a route to ketene in which adsorbed CO couples with a surface methylene; the previously described route couples two CO molecules. No quantum-chemical calculation was involved: "Present CoThinker architecture deliberately bypasses explicit computational chemistry calculations using ab-initio simulations or neural network potentials", and "every mechanistic claim reported herein is derived solely by a frontier reasoning model", identified in the text as OpenAI's GPT-5.4.

Copper-iron oxides at Cu:Fe ratios of 4:1, 3:1, 2:1 and 1:1 were then synthesized and tested. Raising the bicarbonate electrolyte from pH 6.8 to 7.5 increased acetate production rates and Faradaic efficiencies at every composition, most strongly at 1:1. Increasing iron shifted product distribution from formate toward acetate, peaking at 1:1, which the authors read as confirming that iron acts as an electronic modifier. Phosphate electrolytes, which supply protons more readily at the interface, suppressed acetate and passivated the catalyst. The headline figure is "a threefold increase in acetate selectivity over matched Cu-rich baselines" at comparable overall conversion. On the ordering the authors write: "By fixing the mechanistic predictions prior to synthesis, the subsequent electrochemical evaluation serves as a strict forward validation of the predicted control variables rather than a post hoc rationalization of empirical performance."

The scope is one reaction, one catalyst family and one campaign, and the comparison is against the authors' own copper-rich samples; the paper notes that functionalized copper systems reach higher acetate Faradaic efficiencies by other means. Products were quantified by gas chromatography and proton NMR with at least three independent measurements per point. The reaction network was assembled by the authors, so the model's reasoning was constrained by a representation that already encoded their chemical knowledge, and the paper does not report a control in which the same model answered without the network.
