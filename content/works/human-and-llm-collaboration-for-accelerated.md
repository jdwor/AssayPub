---
short: Human versus LLM recipes
title: Human and LLM Collaboration for Accelerated Materials Synthesis and Discovery
authors:
- Gregory Bassen
- Wyatt Bunstine
- Sarah Okandey
- Sarah Cheung
- Elaine Flowers
- Ritwik Bose
- Joshua Hummel
- Christopher D. Stiles
- Maxime A. Siegler
- Tyrel M. McQueen
org: Johns Hopkins University; Johns Hopkins Applied Physics Laboratory
date: 2026-07-08
type: paper
url: https://arxiv.org/abs/2607.07604
links: []
license: arXiv.org perpetual non-exclusive license
beat: physical-world
edition: '001'
well: E2
tier: notice
importance: Notable
novelty: New evidence
evidence: Preliminary
evidence_type: Laboratory test of synthesis recipes written by chemists and by a language model for oxides of one structural
  family, each recipe run twice and checked by X-ray diffraction
independence: Independent
checked:
- Abstract, introduction, results and conclusion read
- Quotations checked against the source
- No errors found in the parts read
found_via: Research agent search.
standfirst: Chemists and a language model each wrote synthesis recipes for the same known and unreported oxides, and
  a laboratory ran every recipe twice. Success rates were about equal within wide error bars. The one new compound
  the study reports came from a chemist's recipe reacting with its platinum crucible.
coi: None found. The authors declare no competing interests.
read: partial
read_gap: The description of the new compound's structure, the methods and the supplementary information, which holds
  the recipes, were not read. The main text does not name the model that wrote the recipes.
---

Computational methods now propose candidate materials far faster than laboratories can make them, and the authors write that "materials discovery using AI/ML tools is limited by the rate with which materials can be experimentally synthesized and characterized". Their study tests one piece of that gap: whether a language model can write a workable synthesis recipe as well as a solid-state chemist can.

The targets are oxides of the Ruddlesden–Popper family, some already reported and some not, chosen because the chemistry is well studied and unmade members are likely to exist. For each target a chemist and a language model wrote a recipe. Each recipe was carried out twice, from the written text alone, and the products were identified by powder X-ray diffraction. If both recipes failed, the results went back to the chemist and the model for a second round.

In the first round the chemists' recipes produced the target for 83% of known compounds and the model's for 75%, with standard errors of 8 and 9 points. For unreported targets the figures were 17% and 22%. The authors conclude that "the LLM does about as well as humans in generating successful synthesis plans for both targeting known materials and discovering new phases (within one standard error of the proportions)". After the second round the rates for known compounds were 79% and 71%, and for unreported ones 22% and 14%, where "the human outperformed the LLM in discovering new phases". The model's recipes were longer and offered alternatives at each step: "The LLM plan, however, is noticeably more detailed than the human plan and regularly provides different options for each step." It failed on one known nickel compound that the chemists made with a recently developed flux technique.

The sample is small, so the intervals around every rate are wide and the two authors of recipes cannot be separated statistically. Success for an unreported target is defined loosely: "For unreported targets, success corresponds to observation and discovery of a new phase by PXRD, which may or may not correspond to the originally intended target." Repeat trials of the same recipe sometimes disagreed, including for a chemist's recipe, which the authors attribute to small differences in furnaces, humidity or starting materials.

The abstract credits the new compound, a barium platinum oxide with a previously unseen structure, to the collaboration between people and model. According to the text, a chemist's second-round recipe used a platinum crucible, and the barium carbonate reacted with the crucible in place of the intended reagent, "yielding single crystals and the serendipitous discovery of" the compound. The data are not yet public: "All data will be made available in an online data repository."
