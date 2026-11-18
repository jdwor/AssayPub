---
short: Faster 3SUM, APSP
title: Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs
authors:
- Josh Alman
- Virginia Vassilevska Williams
org: Columbia University; MIT
date: 2026-10-05
type: paper
url: https://arxiv.org/abs/2610.06783
links:
- kind: material
  label: Lean 4 formalization of the main theorems (Anthropic)
  url: https://github.com/anthropics/formal-math/tree/main/3sum-apsp
- kind: response
  label: 'Karingula and Lovett: a simplified proof with weaker exponents'
  url: https://arxiv.org/abs/2610.15663
  date: '2026-10-11'
- kind: response
  label: 'Saha and Ye: a faster shortest-paths algorithm built on the new matrix routine'
  url: https://arxiv.org/abs/2610.20297
  date: '2026-10-14'
- kind: response
  label: 'Fischer: geometric lower bounds restated under another hypothesis'
  url: https://arxiv.org/abs/2610.32162
  date: '2026-10-23'
- kind: response
  label: 'Chan, Itakura, Ma and Yu: 3SUM without matrix multiplication'
  url: https://arxiv.org/abs/2610.42012
  date: '2026-10-30'
license: CC BY 4.0
beat: mathematics-theory
edition: '004'
well: B1
tier: lead
importance: Major
novelty: New capability
evidence: Compelling
evidence_type: Mathematical proof by two specialists, with the main theorems formalized in Lean 4 by the developer's
  model and re-derived in follow-up preprints by other groups
independence: Independent
checked:
- Abstract, introduction, conclusion and the statement of methods read
- Abstracts of the four follow-up preprints read
- Quotations checked against the sources
- No errors found in the sections read
found_via: Research agent search.
standfirst: Two complexity theorists give the first polynomial speedups over the textbook algorithms for 3SUM and
  all-pairs shortest paths, which refutes two central hypotheses of fine-grained complexity. They state that Claude
  found the algorithm with no human input. Other groups have since simplified and extended it.
coi: The paper states that Claude, made by Anthropic, discovered the algorithm, that an Anthropic model produced
  the Lean formalization, and that Anthropic offered the authors compensation. The model that drafted this assessment
  is also made by Anthropic.
claims:
- claim: 3SUM on integers of polynomial size can be solved deterministically in time with exponent 1.9992, and all-pairs
    shortest paths with polynomially bounded integer weights with exponent 2.9995. This refutes the 3SUM and APSP
    hypotheses.
  status: supported
  note: Both bounds are among the statements formalized in Lean. Karingula and Lovett give a separate proof with weaker
    exponents, and Chan and coauthors reach subquadratic 3SUM by a different algorithm.
- claim: All of the paper's results follow from one algorithm that computes a chosen sparse set of entries of the
    product of two thin matrices in fewer operations than the full product has entries.
  status: supported
  note: Saha and Ye use this theorem to lower the shortest-paths exponent to 2.9964.
- claim: Through known reductions the algorithm also refutes the real-valued versions of both hypotheses, the Exact
    Triangle and Zero-Weight k-Clique hypotheses, and three conjectures on hinted Online Matrix–Vector multiplication.
  status: unverified
  note: The Lean formalization covers Exact Triangle and the zero-weight clique result. The paper does not list the
    real-valued results or the data-structure version among the formalized statements.
- claim: Claude discovered the algorithm in a session that used 16 million output tokens and had no human input.
  status: self-reported
  note: The paper describes the session in one paragraph and links no transcript of it.
read: partial
read_gap: Sections 2 to 5, which contain the algorithm, the reductions and their proofs (about 60 of the 76 pages),
  and the Lean code were not read.
---

3SUM asks whether three of n given numbers sum to zero. All-pairs shortest paths (APSP) asks for the distance between every pair of vertices in a weighted graph. The textbook algorithms take quadratic and cubic time, and decades of work had improved them only by factors smaller than any power of n. Fine-grained complexity turned that record into hypotheses that no algorithm does polynomially better, and derived conditional lower bounds for many other problems from them.

Josh Alman of Columbia University and Virginia Vassilevska Williams of MIT give a deterministic algorithm for 3SUM on integers of polynomial size with running-time exponent 1.9992, and one for APSP with polynomially bounded integer weights with exponent 2.9995. Both follow from one new routine. Given an N-by-D matrix and a D-by-N matrix, with D a small power of N, it computes a chosen sparse set of entries of their product in fewer operations than the full product has entries. The routine modifies a 1982 algorithm of Coppersmith for rectangular matrix multiplication, built on an identity of Schönhage, so that it skips the operations that serve only unwanted entries. Known reductions carry the saving to 3SUM, APSP and their relatives, and the paper lists the first truly subcubic or subquadratic algorithms for tree edit distance, minimum-weight cycle, graph radius and Convolution-3SUM, among others. It reports no progress on CNF-SAT, Orthogonal Vectors, or k-SUM for k of four or more.

The savings in the exponent are small. The authors write that "The new algorithms are algebraic and potentially impractical in their current form", with enormous hidden constants, and that "the exponents can likely be improved".

The paper states that Claude discovered the algorithm. An Anthropic employee had set an internal research model to work on open problems in the theory of cryptography, and "Claude was tasked with verifying and improving the constructions, but instead developed this algorithm, first for the average case, then for the worst case." The paper adds: "The session used 16M output tokens with no human input." Anthropic then "shared the algorithm with the authors in September 2026 under a confidentiality agreement, offered compensation, and provided access to the public version of Claude." The authors simplified and extended it, derived a data-structure version, and wrote the paper. "The authors take full responsibility for this paper." A footnote records that they had earlier tried a similar approach with other matrix multiplication identities, "without success".

After the paper was written, an Anthropic internal model formalized the main theorems in Lean 4, and the code is public. The formalized statements are the bounds for 3SUM, APSP and Exact Triangle and the zero-weight clique result.

Other groups responded within weeks, all in preprints. On October 11, Sankeerth Rao Karingula and Shachar Lovett posted "a simplified proof" of the 3SUM and APSP improvements "with weaker exponents". Barna Saha and Christopher Ye used the matrix theorem to lower the APSP exponent to 2.9964. Timothy Chan and three coauthors gave a randomized algorithm for 3SUM that "completely avoids the use of matrix multiplication", and extended the refutation to k-SUM for odd k, a case the original paper left open. Nick Fischer observed that the lower bounds for geometric problems that rested on the 3SUM hypothesis "have lost their foundation" and restated many of them under a different hypothesis.
