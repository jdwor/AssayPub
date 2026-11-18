---
short: Sixteen agents, one error
title: Divergent strategies and convergent outcomes in autonomous materials discovery
authors:
- Jihan Kim
org: Korea Advanced Institute of Science and Technology (KAIST)
date: 2026-09-21
type: paper
url: https://arxiv.org/abs/2609.23957
links:
- kind: material
  label: Benchmark manifest, charters, audit code, scoring rubric and answer key
  url: https://github.com/jihankim929/replicate-study
license: ''
beat: physical-world
edition: '003'
well: E1
tier: notice
importance: Notable
novelty: New evidence
evidence: Solid
evidence_type: Sixteen replicate week-long agent campaigns on a frozen materials database, half with enforced checks,
  scored against an audit and a reference calculation prepared independently of the agents
independence: Independent
checked:
- Main text read in full, and the methods through the description of the agent runtime
- Quotations checked against the source
- No errors found
found_via: arXiv monitor.
standfirst: Sixteen copies of one research agent, given the same materials database and a week each, took different
  routes to the same set of best methane-storage materials. Fifteen also named the same wrong winner, a database
  entry with part of its structure missing. Checks that made the agents reproduce their numbers did not catch it.
coi: The sixteen agents were sessions of Claude Opus 5, made by Anthropic. Anthropic makes the model that drafted
  this assessment.
read: full
---

Jihan Kim of KAIST gave sixteen separately started sessions of one agent the same open task and compared what they did. Each session ran Claude Opus 5 through Claude Code and received a frozen database of 12,499 metal-organic frameworks, a fixed simulation protocol, a week of computing and the instruction to find the material with the highest deliverable methane capacity. Eight sessions, chosen at random, also had to pass seven enforced checks, one of which was to re-run the headline number from saved inputs. An audit of the database and a reference calculation were prepared apart from the agents and hidden from them. "The investigator made no scientific decisions during the campaign."

The sessions diverged within their first few actions. Some trained surrogate models on small samples, some screened thousands of structures at low accuracy, some worked through structures one at a time, and eight built 2,253 hypothetical structures by modifying database entries. Reported screening ranged from 106 to 5,006 structures. The sessions still arrived at the same leading materials, near 200 cm³ of methane per cm³ of framework. A reference calculation on 2,344 structures found that its nine best were all among those the agents had reported. "Frontier recovery did not scale with search effort": the rank correlation between structures screened and top-ten structures found was 0.10.

Fifteen of the sixteen also named the same wrong winner. The entry they chose is a copper framework whose charge-balancing anions were removed during curation of the database together with the solvent, which leaves empty space that the simulation counts as pore volume. The pre-launch audit had excluded it. At least ten agents recorded signs that the entry was unusual, such as bare copper centers and very low density, and "Each sign was treated as an explanation for exceptional performance rather than a reason to question the structure." One agent calculated a charge of +8 on the copper centers and then balanced it with groups that are not in the file.

All eight checked agents re-derived their headline numbers, against one of the eight unchecked. The checks did not catch the error, because the wrong value reproduces exactly: "The checks therefore changed behavior but did not target the layer at which the decisive error arose." Kim concludes: "Agreement across repeated agents therefore establishes stability to resampling of one model and workflow, not independent confirmation by different data, methods or scientific perspectives."

The paper adds: "These results characterize one model–harness, database and task, not a universal agent failure rate." The model was identified only by an alias, so the runs cannot be repeated on a fixed version. With eight agents in each group, the comparison of checked and unchecked sessions can detect only large differences. A shared-directory fault delivered one agent's files to two others, and excluding those two leaves the conclusions unchanged.
