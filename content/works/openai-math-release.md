---
short: openai/math
title: openai/math
authors:
- OpenAI
org: OpenAI
date: 2026-10-06
type: dataset
url: https://github.com/openai/math
links:
- kind: material
  label: The repository's change history
  url: https://github.com/openai/math/blob/main/history.md
- kind: response
  label: 'Kevin Buzzard: what the Lean code in the release covers'
  url: https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/
  date: '2026-11-12'
license: Apache-2.0
beat: mathematics-theory
edition: '004'
well: B3
tier: lead
importance: Major
novelty: New resource
evidence: Contested
evidence_type: 721 machine-written manuscripts, about 42% with formal proofs in Lean
independence: Self-reported by developer
checked:
- Repository README and change history read in full
- Kevin Buzzard's post read in full
- Quotations checked against the source
- No manuscript was examined
coi: The drafting model is made by Anthropic, a competitor of OpenAI. The critical statements below come from OpenAI's
  own record and from a named expert.
found_via: Research agent search. The monitor's code search did not return it.
standfirst: OpenAI released about 720 mathematical manuscripts written by an internal model, roughly two fifths
  of them with Lean code. It withdrew three the next day because of a sign error. Kevin Buzzard found that for about
  38 manuscripts the Lean code does not state the paper's main theorem.
concerns:
- title: For about 38 manuscripts, the Lean code does not state the main theorem
  body: |
    Kevin Buzzard examined the Lean code in the release and writes: "of the 290 OpenAI theorems which come with Lean code, around 38 of them have the property that the Lean code does not even state, let alone prove, the main theorem of the paper. And OpenAI never claimed that it did!" His example is a manuscript that claims to prove Lech's multiplicity conjecture, where "The headline theorem in the corresponding Lean code can be checked to be Corollary 5.4 of the paper".

    OpenAI's README says the results are "at different stages of verification". A Lean file next to a manuscript does not show that its main result was formally checked: for roughly one in eight of those manuscripts it was not.
  confidence: High. Buzzard is a specialist in formalized mathematics, and the count can be repeated from the public
    repository.
read: partial
read_gap: None of the 721 manuscripts or their Lean files was read. The repository's README and change history were
  read in full.
claims:
- claim: An internal OpenAI model, posed approximately 4,000 problems, produced 721 manuscripts in 373 families,
    using about three hours of computing per result on average.
  status: self-reported
  note: The figures are from the repository's README. The model is not named.
- claim: The manuscripts settle named open problems, among them Kaplansky's direct-finiteness conjecture in characteristic
    two and the symmetric Mahler conjecture.
  status: unverified
  note: Most manuscripts have not been independently checked. On the day after release OpenAI withdrew three and
    revised 14.
- claim: About 42% of the main results have Lean formalizations.
  status: disputed
  note: Kevin Buzzard counts about 38 of the 290 manuscripts with Lean code in which the code does not state the
    paper's main theorem.
- claim: A manuscript added on October 26 refutes the Exponential Time Hypothesis.
  status: unverified
  note: OpenAI says a working group led by Russell Impagliazzo, Ramamohan Paturi and Ryan Williams will examine
    the proof.
---

The repository's README describes its contents as "mathematical manuscripts and supporting proof artifacts produced by an unnamed internal OpenAI model". It lists "721 manuscripts organized into 373 families" and says the model "was posed approximately 4,000 problems", with about three hours of computing per result on average. The catalogue claims results on named open problems, among them Kaplansky's direct-finiteness conjecture in characteristic two and the symmetric Mahler conjecture. OpenAI writes that "these manuscripts are best understood as a form of raw research data, rather than polished academic papers", that "Some of the unformalized results could have issues" and that "We defer to the math community completely on matters of credit, precedence, and concurrent work."

The repository's change history for October 7, the day after release, records that a sign error in one manuscript "invalidates a stabilization-trace cancellation argument and the construction used by two dependent papers", and that "we have withdrawn the following three manuscripts". The same entry says: "We have revised 14 other manuscripts". On October 26 OpenAI added two manuscripts with Lean code. Of one it writes: "The case of 3-SAT refutes the Exponential Time Hypothesis." It adds that "An independent working group of computer scientists led by Russell Impagliazzo, Ramamohan Paturi, and Ryan Williams will examine and explain the proof."

The README says about 42% of the main results have Lean formalizations. Buzzard writes that "for many of the papers in the OpenAI theorem dump" the standard checks on machine-written Lean code "have not yet all been answered affirmatively", and that he has "no reason to believe that any of the tests below will fail".

Most of the manuscripts have not been independently verified, and the share that is correct is unknown.
