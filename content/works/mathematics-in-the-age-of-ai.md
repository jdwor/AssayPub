---
short: Tao on proof abundance
title: Mathematics in the age of AI
authors:
- Terence Tao
org: University of California, Los Angeles
date: 2026-08-17
type: essay
url: https://arxiv.org/abs/2608.16753
links:
- kind: context
  label: The Leiden Declaration on Artificial Intelligence and Mathematics
  url: https://leidendeclaration.ai/
license: arXiv.org perpetual non-exclusive license
beat: mathematics-theory
edition: '002'
well: B5
tier: lead
importance: Major
novelty: New framing
evidence: Not applicable
evidence_type: Argument from the author's account of mathematical practice, conditional on a stated hypothesis
independence: Independent
checked:
- Essay read in full
- Quotations checked against the source
found_via: Research agent search.
standfirst: In the written version of an International Congress lecture, Terence Tao leaves aside what AI can do
  in mathematics and examines the goals of mathematical research. If the tools arrive, the essay argues, solved
  problems will stop being scarce, and the stages after a solution (verification, exposition, acceptance and absorption
  into a field) will limit progress.
coi: None found. The essay discloses that AI assistance was used for literature search, diagrams, autocompletion
  and converting slides to text.
claims:
- claim: Most public evidence about what AI can do in mathematics has not been gathered under controlled conditions
    and is subject to reporting bias.
  status: supported
  note: The essay names the undisclosed variables and cites the First Proof project as a controlled exception. A
    benchmark released three weeks later was designed around these objections.
- claim: If AI tools come to perform a reasonable fraction of research-level tasks, proofs will accumulate faster
    than they can be verified, written up, refereed and absorbed.
  status: unverified
  note: A prediction that depends on a premise the essay asks readers to assume and does not defend.
- claim: Solving a problem is the first of five stages, and the last, in which a result is worked into the standard
    theory of its field, is the most valuable and the least open to automation.
  status: unverified
  note: An argument from the author's experience, with no data offered.
read: full
---

This essay is the written form of Terence Tao's public lecture at the International Congress of Mathematicians in July. It leaves aside what AI tools can do, the subject of most debate, and addresses "what the goals and values of mathematical research actually are".

On capability Tao says only that the evidence is poor. Most of it has "not been gathered under controlled scientific conditions". In the essay's words, "successes are announced and failures are not", and the number of attempts, the human help, the computing cost and the overlap with existing literature usually go unreported. The reader is then asked to assume that the tools will soon do a reasonable fraction of research-level tasks: "I am not asking the reader to want it to be true, to believe that it is true, or to accept it as true; what follows is a conditional analysis."

Under that assumption the essay examines one activity, solving problems. Mathematicians have treated the number of problems solved as a stand-in for their other aims, such as building theory, training students and sustaining a community, because those aims used to advance together. Tao expects them to come apart, by Goodhart's law: "When a measure becomes a target, it ceases to be a good measure." The essay restates the goal five times, each time adding a stage that the first version left out. A solution has to be verified, then clearly written, then accepted by other mathematicians, then worked into the standard theory of its field. Of the last stage Tao writes: "It is also, in my view, the most valuable part of the entire process." Formal verification takes care of the second stage and leaves the others: "We may soon be faced with the very real possibility of a verified proof of a major result that no human understands well enough to explain." Writing can be over-optimized as well. A proof polished by a model can lose the marks of where its author struggled, "leaving a text that is easy to read and hard to learn from".

The prediction that follows is that each stage will back up behind the one before it. "In short, we will transition from an era of proof scarcity to an era of proof abundance", with journals, priority conventions and hiring criteria that were designed for scarcity. For remedies the essay points to the Leiden Declaration of June 2026, endorsed by the International Mathematical Union, and comments on four of its recommendations: disclose tools, make reviewing easier, keep authorship human and attribute properly. Tao adds that if authors cannot give a clear expert-level talk on a result, it should not be published: "A proof that no human can properly explain should be viewed as incomplete, even if it has been formally verified."

The essay argues from experience of the field and presents no data. Its analysis covers problem solving only. Tao writes that theory building, teaching and refereeing need the same treatment and that the conclusions will differ, with the use of AI in training to be restricted "quite tightly".

Three weeks later a benchmark was published that takes the essay's list of undisclosed variables as its design brief ({{frontiermath-erdos}}), and the releases of September and October tested the prediction about abundance ({{navier-stokes-blowup}}, {{openai-math-release}}).
