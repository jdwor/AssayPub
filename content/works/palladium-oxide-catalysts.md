---
short: "Pd-oxide catalysts"
title: AI-guided high-throughput discovery of iridium- and ruthenium-free palladium-oxide catalysts for durable
  acidic oxygen evolution
authors:
- Ken J. Jenewein
- Faezeh Habib Zadeh
- Xiaoxiao Wang
- Gustavo Malkomes
- Huafan Zhang
- Natalie Page
- Jae Jin Bang
- Peter J. Santiago
- Karla V. Contreras
- Katherine K. Li
author_count: 22
org: Lila Sciences
date: 2026-09-24
type: paper
url: https://arxiv.org/abs/2609.30133
license: CC BY 4.0
beat: physical-world
edition: '003'
well: E4
tier: notice
importance: Notable
novelty: New evidence
evidence: Suggestive
evidence_type: Laboratory synthesis and electrochemical testing on thin films, with a retrospective comparison of
  search methods
independence: Self-reported by developer
checked:
- Main text read in full; supplementary information searched but not read
- Quotations checked against the source
coi: All authors are Lila Sciences employees, the company funded the work, and the paper says it has filed or may
  file patents. The language-model baseline that performed worst in the paper's comparison is an Anthropic model,
  and Anthropic makes the model that drafted this assessment.
found_via: Returned by the arXiv monitor (general and infrastructure lenses) and by research agent search.
standfirst: Lila Sciences reports that an automated search across 2,942 catalyst compositions found a palladium
  oxide that held its performance for 1,000 hours in acid. The tests used thin films in a three-electrode cell,
  and all authors are company employees.
read: full
---

Electrolyzers that split water in acid need oxygen-evolution catalysts that resist corrosion. Current ones use iridium or ruthenium, both scarce. Lila's platform combines sputter deposition, automated electrochemical testing and model-guided selection of the next experiments, with people moving samples between stations. The paper says it "iteratively evaluated the activity-stability trade-off of 2,942 catalysts across 53 material systems and 26 elements".

The best catalyst, a palladium oxide with small additions of indium and manganese, kept its overpotential below 0.5 V for 1,000 hours at 10 mA/cm² in sulfuric acid and retained 96% of its palladium. Unmodified palladium oxide passed 0.5 V after about 200 hours. The paper's analysis puts the catalyst at 99.91 atomic percent palladium, a platinum-group metal. The authors write that such catalysts "relax rather than eliminate the supply constraint".

The durability tests were run on thin films in three-electrode laboratory cells, and the 1,000-hour result comes from one film, with shorter repeat runs in the supplement. The benchmarks were ruthenium oxide and palladium oxide films made on the same platform. The paper reports no comparison with an iridium oxide catalyst and no test in a membrane electrode assembly or an electrolyzer. The authors say the cause of the improved durability is not yet established and call for controls that separate the effect of the additives from the film's starting structure.

The authors also compared selection methods retrospectively on the finished dataset. They report that "fixed-policy BO converged similarly to random search and LLM-only selection performed even worse than random search", while their combined agent performed best. The language model in that baseline was Claude Opus 4.6. The comparison was made after the campaign, on a single dataset, with ten repeats per method.

Code and data for the main figures are public.
