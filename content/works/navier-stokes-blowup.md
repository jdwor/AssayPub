---
short: Navier–Stokes blowup
title: Finite Time Blowup for Navier–Stokes
authors:
- OpenAI
org: OpenAI
date: 2026-09-08
type: paper
url: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
links:
- kind: response
  label: 'Constantin, Ignatova and Vicol: what a construction of this kind requires of the force'
  url: https://arxiv.org/abs/2609.20803
  date: '2026-09-17'
- kind: response
  label: 'Bastounis, Circelli and Hansen: the paper and its Lean code differ'
  url: https://arxiv.org/abs/2610.08144
  date: '2026-10-06'
- kind: response
  label: 'Kevin Buzzard: what a Lean check establishes'
  url: https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/
  date: '2026-11-12'
- kind: response
  label: 'Tristan Buckmaster: statement on how the proof was produced'
  url: https://cims.nyu.edu/~tristanb/statement.pdf
- kind: context
  label: The official problem statement (Clay Mathematics Institute)
  url: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
license: ''
beat: mathematics-theory
edition: '003'
well: B2
tier: lead
importance: Major
novelty: New capability
evidence: Contested
evidence_type: A 166-page written proof and a separately released formal proof in Lean
independence: Self-reported by developer
checked:
- Introduction and main theorem of the paper read
- Critique by Bastounis, Circelli and Hansen read through its Navier–Stokes examples; its theoretical sections and
  appendix were not read
- Buckmaster's statement and Buzzard's post read in full
- Abstract and introduction of the paper by Constantin, Ignatova and Vicol read
- Quotations checked against the source; two from Scientific American could not be checked
coi: The drafting model is made by Anthropic, a competitor of OpenAI. Levent Alpöge, whose experience is part of
  the dispute described under Concerns, works at Anthropic according to Buckmaster's statement. Critical statements
  are attributed to named sources and quoted.
quotes_unverified:
- The Clay problem is settled, but the main problem for the Navier-Stokes equations is not.
- We did not use their prompt or proofs to prompt our models.
found_via: Research agent search. The monitor did not find it; the paper is a PDF on a file server with no feed.
standfirst: OpenAI published a 166-page paper under its own name claiming a finite-time blowup for the forced three-dimensional
  Navier–Stokes equations, and released a formal proof in Lean. Other mathematicians dispute how the proof was produced
  and whether the written and formal proofs match.
claims:
- claim: For every positive viscosity there is a solution of the three-dimensional Navier–Stokes equations, driven
    by a smooth and compactly supported force, that starts from rest and blows up in finite time with bounded kinetic
    energy.
  status: unverified
  note: 'Kevin Buzzard reports that the Lean code compiles and is accepted by several independent kernels. The authors
    of the critique write: "The Lean code merely tells us that the theorem is correct".'
- claim: This establishes alternative (C) of the Millennium problem as stated by Fefferman, and alternative (D)
    for the periodic case.
  status: unverified
  note: Alternatives (C) and (D) are the two that allow an external force.
- claim: The Lean code formalizes the results presented in the paper.
  status: disputed
  note: Bastounis, Circelli and Hansen describe two lemmas where the paper and the Lean code differ. Buzzard agrees
    that "there are instances where the pdf proof and the Lean proof diverge".
concerns:
- title: The written proof and the Lean proof differ at specific lemmas
  body: |
    Alexander Bastounis of King's College London and Fabian Circelli and Anders Hansen of the University of Cambridge compared the paper with the Lean code and report that "the formalised Lean proof does not correspond to the NL proof of blow-up of solutions to the Navier-Stokes equations". They give two examples. Lemma 8.6 of the paper bounds a quantity using four more derivatives than it controls, and the corresponding Lean lemma needs five. For the pressure-flux bound in Lemma 10.5, the Lean code proves a different bound by a different argument. They add that "the fact that we display only two examples does not mean that these are the only cases of mistranslations".

    The authors limit their claim: "We do not make claims about the correctness of OpenAI's NL proof, we only make statements about mistranslations into Lean". If they are right, the Lean check supports the theorem and says nothing about whether the written argument is sound.
  confidence: Moderate. The critique is specific and comes from named specialists, and Buzzard independently agrees
    that the two proofs diverge. It is a preprint.
- title: Accounts of how the proof was produced conflict
  body: |
    Tristan Buckmaster of New York University and Levent Alpöge released blowup results for three related equations, obtained with the help of language models. In a statement issued with them, Buckmaster describes calls with OpenAI staff on September 6. He writes that he "was shown a prompt and told the internal research model had simply been given the problem statement", that Alpöge had been told "very little human input" was used, and that "This turned out not to be true." According to the statement, "it emerged that an entire team had been working on the problem". He says it was eventually agreed that the first prompt was sent "after information about our work had reached OpenAI".

    Buckmaster also writes: "I have not seen OpenAI's proof" and "I am not accusing anyone of anything." According to Scientific American, Sébastien Bubeck of OpenAI told a press briefing: "We did not use their prompt or proofs to prompt our models."

    The amount of human direction affects what the result shows about the model's abilities. The paper says nothing on the question.
  confidence: High that the accounts conflict and the matter is unresolved. The record does not show which account
    is correct.
read: partial
read_gap: The proof (sections 2 to 10 and the appendices of the 166-page paper) and the Lean code were not read.
---

The paper constructs, for every positive viscosity, a solution of the three-dimensional incompressible Navier–Stokes equations that "starts from rest and develops unbounded velocity in finite time while maintaining uniformly bounded kinetic energy". The flow is driven by an external force that is smooth and "compactly supported in space and time". The paper states that this "establishes alternative (C) in the Millennium problem statement for Navier-Stokes as stated by Fefferman", and alternative (D) for the periodic case. OpenAI is listed as the only author. The paper does not say how the proof was produced and does not mention the Lean code, which OpenAI released in a separate repository.

The Clay Mathematics Institute's problem statement asks "for a proof of one of the following four statements". Statements (A) and (B) say that smooth solutions always exist when there is no external force. Statements (C) and (D) say that for some initial state and some smooth force no such solution exists. The paper claims (C) and (D). On September 17, Peter Constantin, Mihaela Ignatova and Vlad Vicol posted a proof that in a construction with the features of OpenAI's "the force can neither vanish identically near the singular point, nor be real analytic in the space variables". A singularity built this way needs the force to keep acting at the point where it forms. Scientific American quoted Luis Silvestre of the University of Chicago: "The Clay problem is settled, but the main problem for the Navier-Stokes equations is not."

Kevin Buzzard of Imperial College London writes that the Lean code "is 640K lines of code and compiles fine on my laptop" and "is accepted by multiple kernels as well as Lean's official kernel". The authors of the critique described under Concerns write that the Lean code "merely tells us that the theorem is correct".

Whether the Lean proof corresponds to the written proof, and how much human guidance the model received, are both disputed (see Concerns).
