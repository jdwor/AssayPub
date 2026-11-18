---
short: Two thirds of zeta zeros
title: More than two thirds of the zeta zeros are simple and on the critical line
authors:
- Levent Alpöge
- Ralph Furman
org: Anthropic
date: 2026-08-10
type: paper
url: https://arxiv.org/abs/2608.13637
links:
- kind: material
  label: 'Anthropic: how the result was found'
  url: https://www.anthropic.com/research/riemann-zeta
- kind: material
  label: Lean 4 formalization of the main theorems
  url: https://github.com/anthropics/zeta-23-lean
- kind: response
  label: 'Youness Lamzouri: a simpler proof of the same bounds, with two further estimates'
  url: https://arxiv.org/abs/2609.02882
  date: '2026-09-02'
license: arXiv.org perpetual non-exclusive license
beat: mathematics-theory
edition: '002'
well: B3
tier: lead
importance: Major
novelty: New capability
evidence: Compelling
evidence_type: Mathematical proof checked by two mathematicians at the developer, formalized in Lean 4, and re-proved
  by an outside number theorist
independence: Self-reported by developer
checked:
- Anthropic's post read in full
- Abstract of the paper and its passages on provenance, verification and the method's ceiling read
- Abstract of Lamzouri's paper read
- Quotations checked against the sources
- No errors found in the parts read
found_via: Research agent search.
standfirst: A proof that at least two thirds of the zeros of the Riemann zeta function are simple and lie on the critical
  line, up from a record of 5/12. Anthropic reports that an unreleased version of Claude found it while attempting
  the Riemann hypothesis at the request of a non-mathematician. An outside number theorist has since given a simpler
  proof of the same bounds.
coi: The paper's authors work at Anthropic, whose model found the proof. Anthropic makes the model that drafted this
  assessment.
claims:
- claim: Unconditionally, at least two thirds of the nontrivial zeros of the zeta function are simple and lie on the
    critical line, and at least five sixths are distinct. The previous records were 5/12 and 0.6603.
  status: supported
  note: The two main theorems are formalized in Lean 4 and depend only on Lean's three standard axioms. Youness Lamzouri
    gave a different proof of the bounds three weeks later.
- claim: The proof was discovered autonomously by Claude, in two sessions prompted by a non-mathematician whose input
    was mostly encouragement.
  status: self-reported
  note: Anthropic published transcripts of the process and an account written by the model. The authors checked the
    argument and condensed it into the paper.
- claim: Two thirds is within 0.016 of the most the method can give, and the method is not expected to prove the Riemann
    hypothesis.
  status: supported
  note: Argued in the paper's seventh section. This bound relies on a numerical certification that is not checked
    by the Lean kernel. The main theorems do not depend on it.
read: partial
read_gap: The proof (sections 2 to 6 of the paper) and the Lean code were not read.
---

The Riemann hypothesis says that all the nontrivial zeros of the zeta function lie on one vertical line. Short of proving it, number theorists since Selberg in 1942 have proved that some minimum share of the zeros lie on the line, and the record stood at 5/12. This paper proves, without assuming the hypothesis, that at least two thirds of the zeros are on the line and simple, and that at least five sixths are distinct. Montgomery derived the two-thirds figure in 1973 on the assumption that the hypothesis is true. The new argument removes the assumption. It uses recent work by Aryan and by Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh, and Anthropic's post says: "Claude’s result draws heavily on this line of research, along with a 2000 paper by Bombieri."

The listed authors, Levent Alpöge and Ralph Furman, are mathematicians at Anthropic, and the paper's arXiv record says: "Proof discovered autonomously by Claude (Anthropic); verified and communicated by the listed authors." According to the post, a staff member who is not a mathematician asked an unreleased research version of Claude to "Take a real stab at the Riemann hypothesis". The post continues: "Initially, Claude generated and tried 650 ideas, none of which worked." Prompted to go on, the model coordinated about 60 subagents for a day and a half and arrived at the bound. The operator's "input was mostly limited to sending Claude messages of encouragement". The paper's appendix records the model's first reaction to its own argument: "So this is an extraordinary claim and my prior is that it’s wrong." The two sessions used 31 million output tokens, and Anthropic published transcripts of them.

Alpöge and Furman checked the argument and rewrote it, and "Conrey and Goldston read the manuscript and provided comments". A Lean 4 formalization of the two main theorems is public and depends only on Lean's three standard axioms. On September 2 Youness Lamzouri posted "a new, conceptually simpler, unconditional proof" of the same bounds with two further estimates, and wrote: "The argument produced by Claude is technically intricate, and its main mechanism is not immediately transparent."

Anthropic states the limit of the method: "We don’t expect that the techniques Claude used will lead to proving the Riemann hypothesis." The paper argues that two thirds is within 0.016 of the most its approach can give. That argument is the one place where the paper relies on a numerical certification outside the Lean kernel, and the main theorems do not depend on it.
