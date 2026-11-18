---
short: OpenAI's ten math results
title: Ten Advances in Mathematics and Theoretical Computer Science
authors:
- OpenAI
org: OpenAI
date: 2026-08-01
type: paper
url: https://cdn.openai.com/pdf/ten-proofs-oai.pdf
links:
- kind: material
  label: Lean files for the ten results
  url: https://github.com/openai/ten-proofs
- kind: material
  label: The original version of August 1
  url: https://cdn.openai.com/pdf/ten-proofs-oai-original.pdf
- kind: response
  label: 'Sienicki and Sienicki: an audit of 18 reviews of the ten results'
  url: https://arxiv.org/abs/2608.14673
  date: '2026-08-03'
- kind: response
  label: 'Scientific American: mathematicians object to how prior work was credited'
  url: https://www.scientificamerican.com/article/openais-latest-math-breakthroughs-commit-research-misconduct-experts-say/
  date: '2026-08-06'
license: ''
beat: mathematics-theory
edition: '002'
well: B1
tier: lead
importance: Major
novelty: New capability
evidence: Solid
evidence_type: Ten machine-written proofs in one paper, each with a Lean file, partly examined by outside reviewers
independence: Self-reported by developer
checked:
- Abstract, table of contents and the opening of the first chapter read
- Original and updated versions searched for the citation in dispute
- Scientific American's report read in full, and the abstract and opening sections of the audit
- Quotations checked against the sources
found_via: Research agent search.
standfirst: OpenAI published ten results that it credits to an internal model, among them an explicit non-sofic group
  and a disproof of Connes's rigidity conjecture, each with a Lean file. Outside review has found no confirmed error
  so far. Two mathematicians said the announcement overstated the novelty and under-credited earlier work, and OpenAI
  reissued the paper five days later.
coi: The drafting model is made by Anthropic, a competitor of OpenAI. Critical statements are attributed to named
  sources and quoted.
claims:
- claim: An internal OpenAI model obtained ten new results, among them an explicit non-sofic group, a disproof of
    Connes's rigidity conjecture and a proof of Ehrhart's volume conjecture.
  status: supported
  note: Each result has a Lean file in a public repository. An audit of 18 chapter reviews reports no confirmed error
    in a principal result, says the reviews differ in depth, and records one request for major revision of the proof
    of Ehrhart's conjecture.
- claim: The problems had seen no progress on the main result for at least a decade.
  status: disputed
  note: The wording is from OpenAI's announcement as quoted by Scientific American, which reports that it was later
    changed. Francesco Fournier-Facio and Stephen Miller point to papers of 2016 and 2019 on which two of the proofs
    build.
- claim: The results were obtained by the model.
  status: self-reported
  note: The paper's front matter does not name the model or say how many problems were attempted, what people contributed
    or what the work cost. Scientific American reports the company's figure of $2,000 in tokens.
concerns:
- title: The first version did not cite a 2016 paper that the sphere-packing proof draws on
  body: |
    Scientific American reports that the sphere-packing proof "hinges on a particular mathematical argument that it presented as its own but that actually first appeared in a 2016 paper by Miller and a collaborator". Stephen Miller told the magazine: "It seems completely systematic to me, and it points to research misconduct." The version of August 1 contains no reference to Cohn and Miller. The version of August 6 cites their paper in the first chapter.

    On the non-sofic group, Francesco Fournier-Facio of the University of Cambridge told the magazine that the key step combines ideas from papers of 2016 and 2019, and that the authors of the paper tried to attribute them correctly while the announcement did not: "there is the big PR machine that wants to sound as impressive as possible and does not care about being 100 percent accurate". OpenAI's reply to the magazine was: "We plan to make small updates [to the paper] this week, consistent with standard academic practice."
  confidence: High that the citation was absent and then added, since both versions are public. That the omission
    amounts to misconduct is Miller's judgment.
read: partial
read_gap: Of the paper's 253 pages, only the abstract, the table of contents and the opening of the first chapter were
  read. The proofs and the Lean files were not examined.
---

OpenAI published ten results in one paper of about 250 pages, with a Lean file for each in a public repository. The paper says they were "obtained by an internal OpenAI model". They are spread across mathematics and theoretical computer science: the exact asymptotic strength of the Cohn–Elkies linear program for sphere packing, which gives a better general bound on packing density in high dimensions; improved bounds for binary and spherical codes; an explicit group that is not sofic, which settles whether every countable group is; infinitely many groups that disprove Connes's rigidity conjecture; lower bounds for computing the permanent; exponential parallel repetition for entangled two-player games; hardness of approximating the closest vector problem; the sharp bound in Ehrhart's volume conjecture; a lower bound for multicolor Ramsey numbers; and counterexamples to two conjectures of Erdős in extremal graph theory.

The paper's front matter gives no account of how the results were produced. It does not name the model or say how many problems were tried, what people contributed or what the work cost. Scientific American reports the company's statement that the tokens cost $2,000.

On correctness, the fullest outside record is a preprint by Mikołaj and Krzysztof Sienicki that examines 18 chapter-by-chapter reviews. It concludes: "No surviving confirmed substantive mathematical error in a principal result appears in the assessments examined." It adds: "the reports differ in depth, and several dependencies have only been partly checked". One specialist review asks for major revision of the proof of Ehrhart's conjecture. According to the audit, later work by others confirms that Connes's conjecture is false, without reproducing the paper's stronger result, and proves a stronger form of the closest-vector theorem.

The objections have been about credit and presentation. Scientific American quotes the announcement as saying the problems "have been open and seen no progress on the main result for at least a decade", and reports that the wording was later changed after mathematicians pointed to recent papers that two of the proofs build on. OpenAI reissued the paper on August 6 with a citation added.

Timothy Gowers takes the ten results as the occasion for a post on what kind of mathematics language models are good at ({{gowers-what-maths-are-llms-good-at}}). The authors of FrontierMath Erdős cite announcements of this kind, where the problems attempted and the costs are not disclosed, as the reason for building a benchmark with a fixed list of problems and a fixed budget ({{frontiermath-erdos}}).
