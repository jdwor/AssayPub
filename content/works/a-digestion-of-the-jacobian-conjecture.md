---
short: Jacobian conjecture falls
title: A digestion of the Jacobian conjecture counterexample
authors:
- Terence Tao
org: University of California, Los Angeles
date: 2026-07-21
type: essay
url: https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/
links:
- kind: context
  label: 'Kevin Buzzard: the announcement of the counterexample and its formal verification'
  url: https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/
  date: '2026-07-20'
license: ''
beat: mathematics-theory
edition: '001'
well: B3
tier: lead
importance: Major
novelty: Synthesis
evidence: Compelling
evidence_type: An explicit counterexample that can be checked by direct calculation, formalized in Lean by a third
  party and explained in an independent exposition
independence: Independent
checked:
- Text of the post read in full
- Kevin Buzzard's post of July 20 read in full
- Quotations checked against the sources
found_via: Research agent search.
standfirst: The Jacobian conjecture, open for about a century, is false in three dimensions. The counterexample was
  found with Claude Fable and announced on social media on July 19. Two days later Terence Tao published an explanation
  of why it works, built from the multiplication of low-degree polynomials, and noted one step for which no good
  geometric reason is yet known.
coi: The counterexample was announced by a mathematician at Anthropic and found with an Anthropic model. Anthropic
  makes the model that drafted this assessment. Tao discloses using an AI chatbot to discuss the problem and confirm
  calculations.
claims:
- claim: The Jacobian conjecture is false in three and more dimensions. An explicit polynomial map of degree seven
    in three complex variables has nonzero constant Jacobian and is not invertible.
  status: supported
  note: Tao writes that the example is verified by a brief calculation and gives a construction that explains it.
    Kevin Buzzard reports that Paul Lezeau formalized the counterexample by hand against a statement of the conjecture
    already in Google DeepMind's Formal Conjectures repository.
- claim: The counterexample was found using Claude Fable.
  status: self-reported
  note: Tao states it in a parenthesis. Buzzard attributes the announcement to a post on X by Levent Alpöge. Neither
    post describes how the model was used.
- claim: The conjecture remains open in two dimensions.
  status: supported
  note: Stated by Tao. The counterexample needs a third variable.
read: partial
read_gap: The post's formulas are embedded as images and were not legible in the text that was read, so the calculation
  itself was not followed. The original announcement on X was not read.
---

The Jacobian conjecture says that a polynomial map of complex n-dimensional space to itself whose Jacobian determinant is a nonzero constant must have a polynomial inverse. Put another way, a polynomial map that is invertible near every point is invertible everywhere. Tao writes: "It was recently shown (using the Fable AI) that the conjecture is false in three dimensions (and thus in higher dimensions as well)". The post adds: "The conjecture remains open in two dimensions, and is easy to establish in one dimension."

The counterexample is an explicit map of degree seven in three variables. Anyone can confirm by direct calculation that its Jacobian is constant and that it sends distinct points to the same point. The post says of it: "While this is an extremely quick verification, the construction presented in this fashion appears like a massive miracle." A map of that degree would ordinarily have a Jacobian with a great many nonconstant terms, all of which have to cancel, "So finding such a polynomial looks highly unlikely to be located by brute force."

To explain the map, Tao splits the task into three requirements, a map that is locally injective, that is not globally injective, and whose domain is a copy of three-dimensional space, and builds toward each separately. The raw material is the map that multiplies a linear polynomial in two variables by a quadratic one to give a cubic. A generic cubic factors in three ways, which supplies the failure of global injectivity, and a normalization supplies local injectivity. The domain is then cut down to three dimensions by a hyperplane, and for one special class of hyperplane the result turns out to be equivalent to ordinary three-dimensional space. On that step Tao writes: "I do not have a completely satisfactory geometric explanation for this miracle". The construction recovers the original example up to changes of variable.

Kevin Buzzard's post of the day before ({{human-mathematicians-are-being-outcounterexampled}}) gives the circumstances. Levent Alpöge announced on X that Fable had found the counterexample. Buzzard wrote: "This is a big deal — this is a famous question in algebraic geometry which had been open for 100 years and which many people had thought about." By the next morning, the post reports, "Paul Lezeau had already formalized the counterexample manually" in Lean. Buzzard added: "The next step in that work is for humans to understand exactly what is going on with the example." Tao's post is a first installment of that.

Neither post says how the model was prompted or how much its user contributed. The post ends with a disclosure: "AI disclosure: I used an AI chatbot to discuss various aspects of this problem and to confirm several of the calculations made here."
