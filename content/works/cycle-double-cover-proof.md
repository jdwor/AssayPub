---
short: Cycle double cover proved
title: A Proof of the Cycle Double Cover Conjecture
authors:
- OpenAI
org: OpenAI
date: 2026-07-10
type: paper
url: https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf
links:
- kind: material
  label: Lean formalization of the theorem
  url: https://github.com/openai/cdc-lean
- kind: response
  label: 'Sang-il Oum: an exposition of the proof with slight modifications'
  url: https://arxiv.org/abs/2607.16356
  date: '2026-07-17'
license: ''
beat: mathematics-theory
edition: '001'
well: B1
tier: lead
importance: Major
novelty: New capability
evidence: Compelling
evidence_type: A three-page proof from known theorems and linear algebra, with a Lean formalization and an independent
  exposition by a graph theorist
independence: Self-reported by developer
checked:
- Note read in full
- Abstract of Sang-il Oum's exposition read
- Quotations checked against the sources
- The Lean repository was not examined
- No errors found
found_via: Research agent search.
standfirst: A three-page note from OpenAI proves the cycle double cover conjecture, a problem in graph theory open since
  the 1970s, and states that the proof is entirely the work of a language model. The argument combines a known theorem
  on flows with elementary linear algebra. A graph theorist published his own exposition of it a week later.
coi: The drafting model is made by Anthropic, a competitor of OpenAI.
claims:
- claim: Every finite bridgeless undirected graph has a cycle double cover.
  status: supported
  note: The proof is three pages long. Sang-il Oum posted an exposition that presents it with slight modifications,
    and OpenAI published a Lean formalization.
- claim: The proof is entirely due to GPT 5.6 Sol Ultra.
  status: self-reported
  note: The note has one sentence on the use of AI. It gives no prompts and does not say how many attempts were made
    or how the problem was chosen.
- claim: The proof needs only the reduction to cubic graphs, the 8-flow theorem of Jaeger and Kilpatrick with a result
    of Tutte, and an elementary linear algebra argument.
  status: supported
  note: The note cites each ingredient and remarks that Seymour's stronger 6-flow theorem is not needed.
read: full
---

A cycle double cover of a graph is a collection of cycles in which every edge appears exactly twice. The conjecture that every graph without a bridge has one was posed in the 1970s by Szekeres and by Seymour, among others, and had been proved only for special classes such as planar graphs. The note states the full result: "Theorem 1.1. Every finite bridgeless undirected graph has a cycle double cover."

The proof takes three pages and uses no new machinery. By a standard reduction it is enough to treat cubic graphs, in which three edges meet at every vertex. A theorem proved independently by Jaeger and Kilpatrick in the 1970s gives every bridgeless graph a labeling of its edges by nonzero vectors of length three over the field with two elements, summing to zero at each vertex. The new step turns that labeling into an assignment of a pair of vectors to each edge, such that every vector appears on either none or two of the three edges at a vertex. The edges carrying a given vector then form disjoint cycles, and together those cycles cover every edge twice. Showing that the pairs can be chosen consistently at both ends of every edge comes down to the solvability of a system of linear equations, which the note proves by a duality argument. The note says: "This reduction eventually reduces to an elementary linear algebra argument."

On authorship the note says: "Statement of AI use. The proof in this note is entirely due to GPT 5.6 Sol Ultra and the writeup with Codex (with GPT 5.6 Sol)." It gives no prompts and does not say how many attempts were made, who chose the problem, or who checked the output before release.

The result is unusual among the year's AI-attributed proofs in being short enough for a specialist to read at a sitting. Sang-il Oum, a graph theorist, posted an exposition on arXiv a week later: "This exposition presents the proof with slight modifications intended to make it more accessible." OpenAI also published a Lean formalization. Most of the manuscripts in OpenAI's later bulk release ({{openai-math-release}}) have had no such reading.
