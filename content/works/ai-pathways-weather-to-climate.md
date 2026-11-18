---
short: Weather to climate
title: Artificial intelligence pathways from weather to climate
authors:
- Tom Beucler
- J. David Neelin
- Hui Su
- Shivanshi Asthana
- Chris Bretherton
- Will Chapman
- Costa Christopoulos
- Spencer K. Clark
- Aditya Grover
- Ignacio Lopez-Gomez
- Tapio Schneider
- Adam Subel
- Oliver Watt-Meyer
org: University of Lausanne; UCLA; Allen Institute for AI; Caltech; Google Research and others
date: 2026-10-07
type: paper
url: https://arxiv.org/abs/2610.09770
links:
- kind: material
  label: Data behind the paper's first and ninth figures
  url: https://doi.org/10.5281/zenodo.22872186
license: CC BY 4.0
beat: physical-world
edition: '004'
well: E2
tier: notice
importance: Notable
novelty: Synthesis
evidence: Suggestive
evidence_type: Narrative review by developers of several of the models discussed, with one original comparison
  of reported model speeds
independence: Independent
checked:
- Paper read in full
- Quotations checked against the source
- No errors found
found_via: arXiv monitor.
standfirst: Thirteen researchers, among them developers of leading learned weather and climate models, review what
  such models do in forecasting and set out what climate projection requires of them. They argue that a learned climate
  model must take each forcing as a separate input and be tested outside its training conditions, and they report cases
  where their own emulators failed such tests.
coi: Several authors developed models the review uses as case studies, among them ACE at the Allen Institute for
  AI and CliMA at the California Institute of Technology. Two authors are affiliated with Google Research. The authors
  declare no competing interests.
read: full
---

Thirteen authors from universities, the Allen Institute for AI, Google Research and NOAA review what learned models now do in weather forecasting and ask what it would take to extend them to climate projection. The paper has been submitted to Science Advances. The authors include developers of several of the systems discussed, and they write that "we illustrate these steps with models the authors have helped develop, including design choices and failure modes".

The review starts from the dependence of data-driven forecasting on the older kind. The leading learned forecasters are trained and scored on reanalyses made with dynamical models, start from initial states that those models produce, and at longer lead times often take dynamical forecasts as input. "AI therefore shifts, rather than removes, the need for dynamical modeling." At lead times of two to six weeks, one benchmark cited in the review found that models built for weather lose skill quickly, "often underperforming climatology after about 10 days", and in ECMWF's 2025 forecasting competition methods that post-process or combine dynamical forecasts performed strongly.

The authors write that "Climate projection is not simply weather forecasting extended to longer lead times." A climate model has to give the statistical response to forcings, such as greenhouse-gas concentrations, that lie outside the observed record and that have risen together within it. The authors propose two minimum requirements for a learned climate model. Each forcing agent has to enter the model explicitly enough to be varied independently of the others, and the model has to be tested outside its training distribution, on extremes and on counterfactual scenarios.

The section on the ACE emulator, written by its developers, reports the results of such tests. A version trained on historical simulations, then run with observed sea-surface temperatures and carbon dioxide held at its 1979 level, warmed too little. A version coupled to a simple ocean was trained on climates with one, two and four times present carbon dioxide and reproduced an unseen climate with three times. When carbon dioxide was quadrupled abruptly, though, its atmosphere reached the new equilibrium in about 90 days, which breaks energy conservation. Adding training simulations in which sea-surface temperature and carbon dioxide vary independently improved the separation of the two effects. Testing an emulator against held-out simulations has a limit of its own: "such tests establish fidelity to the reference, not to Earth". The review also reports that "Lower short-range forecast error does not guarantee lower climate bias", so models have to be chosen on long simulations.

In a new analysis, the authors compare the reported speeds of GPU-based dynamical models, hybrid models and learned emulators. Once the number of variables and vertical levels and the length of the time step are taken into account, most of the apparent speed advantage of the learned models disappears, and the authors conclude that "much of AI's time-to-solution gain arises from computing less". They caution that "this descriptive fit is not a scaling law": the figures were reported under different benchmarking conditions and leave out the cost of training. On learned correction of climate-model biases for local projections, the review says "its advantage over established statistical methods is not yet clear-cut".

The review is narrative and does not say how its literature was selected.
