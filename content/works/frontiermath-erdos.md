---
short: Erdős benchmark
title: FrontierMath Erdős
authors:
- Tom Adamczewski
- Thomas F. Bloom
org: Epoch AI; University of Manchester
date: 2026-09-06
type: benchmark
url: https://arxiv.org/abs/2609.25050
links:
- kind: material
  label: The benchmark's Lean statements and evaluation code
  url: https://github.com/epoch-research/LeanOpenProblems
- kind: context
  label: 'Thomas Bloom: the Erdős problems site, with pages for each problem'
  url: https://www.erdosproblems.com/
license: CC BY 4.0
beat: infrastructure
edition: '003'
well: G2
tier: lead
importance: Major
novelty: New resource
evidence: Solid
evidence_type: Five models run once each on 68 open problems chosen in advance, under a fixed budget, with every solution
  checked as a formal proof in Lean
independence: Independent
checked:
- Main text read in full, with the appendix summarizing the five solutions
- Quotations checked against the source
- The Lean proofs were not examined
- No errors found
found_via: Research agent search.
standfirst: A benchmark of 68 open Erdős problems, chosen in advance and stated in Lean, was given to five models
  with $300 and no human help per problem. One model resolved two and the rest none. In further attempts costing over
  $220,000 the same model resolved three more, among them Erdős's 1931 conjecture on distinct subset sums and the
  Erdős–Sós conjecture, with proofs that are machine-checked and not yet digested by mathematicians.
coi: Claude Fable 5.1 and Claude Fable 5, made by Anthropic, are among the models tested and resolved no problem.
  Anthropic makes the model that drafted this assessment. The authors had a pre-release version of OpenAI's GPT-6 Astra,
  and the paper does not say how that access was arranged.
claims:
- claim: Given $300, 72 hours and no human guidance per problem, a pre-release GPT-6 Astra resolved 2 of 68 open Erdős
    problems, and four other models resolved none.
  status: supported
  note: Each accepted proof passed a checker that replays it through the Lean kernel against a trusted statement. The
    Astra runs were metered at another model's prices, and the authors corrected the costs afterward and excluded one
    resolution.
- claim: In further attempts with larger budgets the same model resolved five of the 68, including a disproof of the
    distinct-subset-sums conjecture and a proof of the Erdős–Sós conjecture.
  status: supported
  note: These proofs passed the same checker. The attempts did not follow the benchmark protocol, and the authors say
    they should not be read as a benchmark score.
- claim: The problems were selected so that a solution by a person would merit a paper in a high-level journal.
  status: self-reported
  note: One author made the selection and calls it "a very personal and subjective judgement".
- claim: At a 3% success rate and $300 per attempt, the expected cost of a resolution is roughly $10,000.
  status: supported
  note: This follows from two resolutions in 68 attempts. The five resolutions across all attempts cost over $220,000.
read: full
---

Reports of AI systems solving open problems have come mostly from the companies that built them, one success at a time. The authors cite Terence Tao's objections to evidence of that kind and put the first of them this way: "announced solutions are a numerator without a denominator". Their benchmark fixes the list of problems in advance. Thomas Bloom of the University of Manchester, who runs the site erdosproblems.com, chose 68 conjectures from the 652 problems then open on it, taking those whose resolution by a person would merit a paper in a high-level journal. Each is stated in Lean, and a model must prove the statement or its negation. A submission counts only if it passes Comparator, a checker from the developers of Lean that replays the proof through Lean's kernel against the trusted statement and permits only the standard axioms. Under those rules, the paper says, "an accepted proof is a proof".

Five models each made one attempt per conjecture, with $300, 72 hours, no network access and no human guidance. "One (GPT-6 Astra) scored 3%, and all others scored 0%." The others were GPT-5.6 Sol, GPT-5.5, Claude Fable 5.1 and Claude Fable 5. Astra, in a pre-release version, resolved two conjectures. It disproved one about graphs that are close to bipartite and proved one about the primes that divide sums of pairs from a set.

The paper also reports attempts made outside the protocol, with larger budgets and varied settings, and labels them: "These attempts do not follow the protocol of Section 3.4 and should not be read as a benchmark score." In them Astra resolved three more conjectures. One is a disproof of the conjecture on sets with distinct subset sums, which dates to 1931 and which Erdős called "perhaps my first serious problem". Another is a proof of the Erdős–Sós conjecture on trees in graphs, which the paper cites as "one of the most tantalizing problems in extremal graph theory". Of that proof the appendix says: "The proof is surprisingly short and elegant." The third is a conjecture of Erdős and Simonovits on the Turán numbers of bipartite graphs. "Reaching these 5 resolutions took over $220,000 of compute across all attempts, compared to roughly $20,000 for the benchmark run itself." Fifty-six other conjectures were tried between two and five times, and none was resolved.

The proofs have been checked by machine and have not yet been absorbed by mathematicians. The appendix gives a few paragraphs on each and says: "These informal expositions should be viewed as placeholders". The authors note that a model may find an argument and fail to formalize it, so "FME scores may therefore substantially underestimate mathematical ability." Problems that are solved may enter the training data of later models. The Astra runs were metered at the prices of a cheaper model, which gave each attempt nearly twice the intended budget. The authors recomputed the costs and dropped one resolution from the benchmark score. They summarize: "The capability is also both new and limited: only the newest model we evaluated displayed it, and 63 of the 68 conjectures remain open."
