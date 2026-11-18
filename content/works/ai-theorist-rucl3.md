---
short: Agents explain a magnet's spectra
title: The AI Theorist reveals excitonic structure in α-RuCl₃
authors:
- Hongjian Zhou
- Xianfan Nie
- Sean Wu
- Tarun Patel
- Jinge Wu
- Andrew Liu
- Adam Wei Tsen
- David A. Clifton
org: University of Oxford; University of Waterloo; Stanford University; University College London
date: 2026-10-01
type: paper
url: https://arxiv.org/abs/2610.02417
links: []
license: CC BY 4.0
beat: physical-world
edition: '004'
well: E1
tier: notice
importance: Notable
novelty: New capability
evidence: Preliminary
evidence_type: One case study in which language-model agents ran first-principles calculations to explain the authors'
  own unpublished spectra
independence: Self-reported by developer
checked:
- Paper read in full, including methods
- Quotations checked against the source
- No errors found
found_via: arXiv monitor.
standfirst: A system of language-model agents ran first-principles calculations to explain new optical measurements
  of a quantum magnet, and proposed that its low-energy peaks are excitons that respond to different polarizations
  of light. The account rests on one case, its prediction has not been tested, and the data and code are not yet released.
coi: The authors built the system and made the measurements it explains. Four of its five agents run on Claude Opus
  4.6, made by Anthropic, which also makes the model that drafted this assessment.
read: full
---

α-RuCl₃ is a layered magnetic insulator studied as a candidate for a Kitaev quantum spin liquid. Experimenters among the authors measured the reflection and photocurrent spectra of a thin crystal at 8 K and found three low-energy peaks and a higher one, which differ in prominence between the two measurements. The spectra had not been published. The paper reports that a system of language-model agents, AI Theorist, then built an explanation for them from first-principles calculations.

The system gives each agent a role. One proposes hypotheses from the data and the literature, one designs calculations, one runs them with standard electronic-structure and many-body codes (Quantum ESPRESSO and BerkeleyGW), one criticizes the results, and one writes the synthesis. Claude Opus 4.6 fills four of the roles, and a fine-tuned open model, Qwen3.5-27B, designs the calculations. The paper says the agents tried and rejected two explanations before settling on a third, in which the low-energy peaks are bound excitons that appear in the calculation only when spin–orbit coupling and electron–hole interactions are both included. Two of the excitons, about 0.11 eV apart, couple to light polarized along different in-plane directions. That gives a prediction: rotating the polarization should strengthen one peak relative to the other. The investigation used 154 million tokens, and its longest sequence of calculations took 38.5 hours.

The authors claim "the first demonstration of an AI system autonomously developing a physical model to explain previously unpublished experimental observations in a quantum material". People chose the question and made the measurements: "Human contributions include setting the research direction, conducting the measurements and providing experimental context."

The paper calls the peak assignments candidates. In the calculated spectrum two of the three low-energy features "do not form distinct maxima in the unshifted, in-plane-averaged spectrum". The calculations with and without spin–orbit coupling used different grids and pseudopotentials, so comparing them "does not isolate SOC alone". Grid tests were made "without establishing convergence of the mean-field or screening calculations". The polarization prediction has not been measured.

The check by a person takes one sentence: "Subsequent analysis by an independent human theorist corroborates the numerical methods and microscopic interpretations." The theorist is not named and the analysis is not shown. The data, including the record of the calculations, "will be shared in a public repository once available", and the paper says the same of the code and prompts. Until then the agents' decisions, and any human intervention in them, cannot be examined.
