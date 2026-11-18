---
short: Fermat formalized in Lean
title: Formalizing Fermat's Last Theorem
authors:
- Anthropic
org: Anthropic
date: 2026-09-04
type: lab-report
url: https://www.anthropic.com/research/formalizing-fermats-last-theorem
links:
- kind: response
  label: 'Kevin Buzzard: what the formalization is and what it is not'
  url: https://xenaproject.wordpress.com/2026/09/04/flt-anthropic-has-beaten-me-to-it/
  date: '2026-09-04'
- kind: response
  label: 'Kevin Buzzard: compiling the code, in a post on what a Lean check establishes'
  url: https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/
  date: '2026-11-12'
- kind: context
  label: 'Chen and coauthors: the Prove2Me platform the agents worked on'
  url: https://doi.org/10.48550/arXiv.2608.28433
license: ''
beat: mathematics-theory
edition: '003'
well: B1
tier: lead
importance: Major
novelty: New capability
evidence: Solid
evidence_type: A formal proof of 13 million lines that the Lean proof assistant accepts, compiled and inspected
  by one outside expert
independence: Self-reported by developer
checked:
- Anthropic's report read in full
- Kevin Buzzard's post of September 4 read in full, and the passage on this proof in Buzzard's post of November
  12
- Quotations checked against the sources
- The Lean code was not examined
- No errors found
found_via: Research agent search.
standfirst: Anthropic reports that Claude agents wrote a complete formal proof of Fermat's Last Theorem in Lean
  in 11 days, a task the community project expected to take years. Kevin Buzzard, who leads that project, compiled
  the code and confirms that it checks. Buzzard adds that the proof was never in doubt and that the result shows
  how much can now be formalized automatically.
coi: The work is Anthropic's, and Anthropic makes the model that drafted this assessment. Anthropic lent Kevin Buzzard
  the machine used to compile the code.
claims:
- claim: The repository contains a complete proof of Fermat's Last Theorem that Lean accepts, using only Lean's
    three standard axioms and proving Mathlib's own statement of the theorem.
  status: supported
  note: Kevin Buzzard compiled the code, ran the comparator on it and inspected by hand the parts that are neither
    definitions nor proofs.
- claim: This is the first complete computer-checked proof of the theorem.
  status: supported
  note: Buzzard, who leads the community project to formalize the theorem, confirms it. The proof adapts parts of
    that project and of an earlier formalization for regular primes.
- claim: Claude agents wrote the proof in 11 days, working largely autonomously, with human mathematical input limited
    to occasional high-level instructions.
  status: self-reported
  note: Anthropic publishes excerpts of the model's reasoning and two examples of the instructions. It reports that
    earlier attempts on a different setup failed.
- claim: The work consumed about six billion output tokens from an internal research model and produced 13 million
    lines of Lean.
  status: self-reported
  note: Buzzard counts over 13.4 million lines. The report gives no cost.
read: full
---

Anthropic reports that Claude wrote a complete proof of Fermat's Last Theorem in the Lean proof assistant: "We are sharing the first complete computer-checked proof of Fermat’s Last Theorem." A community project to formalize the theorem, begun in 2024 under Kevin Buzzard of Imperial College London, was expected to take years.

The proof runs to 13 million lines of Lean and uses 29,500 intermediate theorems. It follows the 1995 exposition of Wiles's argument by Darmon, Diamond and Taylor, and adapts parts of Buzzard's project and of an earlier formalization for regular primes. The report says that dozens of Claude agents worked for 11 days and consumed "about six billion output tokens from a general-purpose internal research model roughly comparable to Claude Fable 5.1". "Mathematical input from humans was limited to occasional high-level instructions" from Tianyi Peng, an Anthropic researcher. The first attempts failed, because the agents "quickly lost track of the project’s state and stopped collaborating effectively". The effort succeeded on Prove2Me, a platform from Peng's group at Columbia University that keeps a graph of theorem statements for the agents to work from.

The report says the finished proof "uses just Lean’s three standard axioms, and a comparator confirmed that the theorem’s statement matches Mathlib’s own statement of FLT". Buzzard checked this independently and wrote on the day of the announcement: "I’ve compiled the code base and run comparator on it — it checks out." Compiling took a machine with 96 cores and 500 gigabytes of memory, which Anthropic lent, and nearly 20 times as long as compiling Lean's mathematics library. Buzzard also "manually inspected every line of the code base which (according to Claude) was not a mathematical definition or proof of a theorem, and verified that none of it was doing anything malicious." Four days later OpenAI released a Lean proof for its Navier–Stokes claim, and the dispute there turned on whether the code matched the written argument ({{navier-stokes-blowup}}). Here the statement proved is the library's own.

Buzzard writes: "Note that mathematically this work of anthropic tells us essentially nothing", since the proof was not in doubt and "the formalization just faithfully follows the early literature on the proof and adds nothing". Buzzard takes it as evidence of what automatic formalization can now do: "If thousands of pages of the literature can be formalized end-to-end by some kind of AI swarm in an 11 day period now, then in the future we will start to see formalization of modern research being done on the fly." Buzzard's own project continues. It aims at the modern proof, at contributions to Lean's library, and at a document in which people can explore the argument.

Anthropic notes that "our proof is likely much longer than it needs to be", and the report gives no cost. Buzzard writes: "I was given £1M to run my project over 5 years; Anthropic took only 11 days but I do wonder if they spent more money…" How much the people involved contributed rests on Anthropic's account, with excerpts of the model's reasoning as the published record.
