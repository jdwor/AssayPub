---
short: When to trust black boxes
title: 'Headlines and inside stories: understanding and trust in AI for mathematics, science, and engineering'
authors:
- Tapio Schneider
org: California Institute of Technology, on Terence Tao's blog
date: 2026-09-23
type: essay
url: https://terrytao.wordpress.com/2026/09/23/headlines-and-inside-stories-understanding-and-trust-in-ai-for-mathematics-science-and-engineering/
links: []
license: ''
beat: physical-world
edition: '003'
well: E3
tier: notice
importance: Notable
novelty: New framing
evidence: Not applicable
evidence_type: Argument with examples from weather forecasting, climate projection and aircraft design
independence: Independent
checked:
- Essay read in full
- Quotations checked against the source
found_via: Research agent search.
standfirst: A climate scientist extends the mathematicians' complaint about undigested proofs to science and engineering.
  The essay argues that a black-box model can be trusted where its predictions are checked quickly, as in weather
  forecasting, and that predictions which cannot be checked in time, such as climate projections, need a chain of
  reasoning that can be audited link by link.
coi: The author works on CliMA, a climate model built in the way the essay recommends, and the essay is cross-posted
  on that project's blog.
read: full
---

Tapio Schneider, a climate scientist at Caltech, takes up an argument that mathematicians made after OpenAI's Navier–Stokes announcement ({{navier-stokes-blowup}}): a proof that no one has digested delivers a result without understanding. The essay quotes Yehuda Rav, "theorems are the headlines, proofs are the inside story", and argues that the point carries over to natural science and engineering, where understanding also decides which predictions can be trusted.

The criterion offered is how soon a prediction can be checked. "A black-box AI weather prediction model can predict tomorrow’s weather, and we can trust it because its forecasts can be checked every day." A protein structure predictor can be checked against experiment. For a climate projection decades ahead, or the certification of a new aircraft, the check comes too late or costs too much, and then "an auditable causal chain from assumptions and input data to the predicted outcomes is what makes predictions trustworthy". Computational fluid dynamics has such a chain: numerical methods with a theory of stability and convergence, and models of unresolved turbulence whose assumptions can be tested one at a time. An end-to-end learned weather model has none. It contains no pathway by which greenhouse gases change the weather it has learned, and it does not enforce conservation of energy, so the essay would not trust it for climate projection. "Nor would we trust an AI surrogate of CFD simulations to certify an aircraft of novel shape."

Schneider's recommendation is to "embed AI at the links in the chain where trust can be earned by empirical verification". Known equations and conservation laws govern the large scales, and models of small-scale processes are learned from data, on the ground that the same local physics holds in conditions not yet observed. The essay notes that a learned small-scale model can still fail if its training data do not span the conditions it will meet. It compares the arrangement with AI in mathematics, where agents propose and a verifier checks. "In the case of mathematics, the checks are complete; in the case of turbulence closures, they are limited to the conditions covered, so trust is restricted to the tested conditions."

On the Navier–Stokes result, Schneider observes that the equation ceases to be physically valid at the small scales where the claimed singularity forms, so that "the result says little about how we model, predict, and understand the physical phenomenon of turbulence".

The essay is an argument with examples and presents no new evidence.
