---
short: AI counterexamples, checked in Lean
title: Human mathematicians are being outcounterexampled
authors:
- Kevin Buzzard
org: Xena Project blog; Imperial College London
date: 2026-07-20
type: essay
url: https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/
links: []
license: ''
beat: mathematics-theory
edition: '001'
well: B2
tier: notice
importance: Notable
novelty: New evidence
evidence: Suggestive
evidence_type: First-hand account by a specialist in formalized mathematics of results he compiled and checked in
  Lean
independence: Independent
checked:
- Post read in full
- Quotations checked against the source
found_via: Research agent search.
standfirst: Kevin Buzzard recounts two months in which AI systems produced counterexamples to three long-standing
  conjectures and formalized them in Lean, and says what he checked himself in each case. One check, of a counterexample
  to a question of Grothendieck, took him under five minutes.
coi: Buzzard maintains Lean's mathematics library and says so in the post. The workshop the post describes was sponsored
  by a company that sells an autoformalization tool, and OpenAI gave its attendees free access. Buzzard is quoted
  as a reviewer in other assessments.
read: full
---

Kevin Buzzard leads the community effort to formalize Fermat's Last Theorem in Lean, and this post is a dated record of what reached that community between May 20 and July 20.

The first case is the disproof of Erdős's unit distance conjecture, announced by OpenAI in May. Within a week a company had formalized the reduction of the counterexample to a deep theorem of number theory. A month later an OpenAI researcher steered a model to a formalization of the whole argument, including the number theory, which takes more than a hundred pages on paper. Buzzard notes that "Sol had generated 1.2 million lines of Lean code in the three weeks that it had worked on the project", about half the size of Lean's mathematics library, which took nine years to write. "One cannot trust AI-generated code so I ran it in a sandbox on my machine", and it compiled.

The second case arose at a workshop Buzzard ran in July. A participant, Akhil Mathew, raised a question of Grothendieck from the 1960s, whether every finite free group scheme of order n is killed by n. Four days later Mathew sent a twelve-page counterexample found by an OpenAI model. Buzzard writes: "I immediately replied saying that I was not reading AI-generated informal mathematics and could he please formalize the entire thing in Lean." A second model produced a 1,076-line Lean file in four hours. Buzzard checked that the statement used only definitions from the trusted library, that it said what was claimed, and that the proof compiled, and "it took me under 5 minutes in total". "At this point I knew that we had a counterexample — a group scheme of order 4 which was not killed by 4."

The third is the Jacobian conjecture ({{a-digestion-of-the-jacobian-conjecture}}), announced the night before the post. A human had formalized that counterexample by morning, helped by the fact that the statement of the conjecture was already in a public repository. Buzzard concludes: "The importance of formalization of conjectures by humans is that if humans are agreed that a Lean statement does faithfully capture the idea behind a conjecture, then checking that (possibly AI-generated) Lean code does comprise a proof or disproof of the conjecture is a triviality."

The post also reports how working habits changed. A doctoral student finished a formalization project of 250,000 lines in about two weeks with the new models, and Buzzard told a skeptical colleague that "any PhD student who was not paying $200 per month to access these tools was crazy". The post ends: "For the true value of work like this is to give humans better understanding of mathematics."

This is one person's account, written quickly, and all three cases are counterexamples, which are short to state and check compared with proofs. The post does not discuss failed attempts.
