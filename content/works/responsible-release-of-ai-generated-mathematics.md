---
short: Release rules for AI proofs
title: Responsible Release of AI-Generated Mathematics
authors:
- François Charles
- Camillo De Lellis
- Timothy Gowers
- Martin Hairer
- Nikhil Srivastava
- Ulrike Tillmann
- Ravi Vakil
- Edward Witten
- Melanie Matchett Wood
org: Advisory Group on Mathematics and Artificial Intelligence
date: 2026-09-29
type: policy-report
url: https://agmai.org/general-sep29/
links:
- kind: material
  label: The group's page, with its membership and its later statements on OpenAI's releases
  url: https://agmai.org/
license: ''
beat: institutions
edition: '003'
well: H4
tier: notice
importance: Notable
novelty: New framing
evidence: Not applicable
evidence_type: Recommendations from a nine-member advisory group, informed by a survey of mathematicians
independence: Independent
checked:
- Guidelines read in full
- The group's page read for its membership, origin and statement of October 6
- Quotations checked against the sources
found_via: Research agent search.
standfirst: Nine mathematicians, organized as an independent advisory group after an approach from OpenAI, set out
  what an AI company should do when it releases mathematics that no person yet understands. They ask for the model,
  prompts and cost to be disclosed, for results to go to repositories the companies do not control, and for the
  companies to pay for the work of understanding without directing it.
coi: The drafting model is made by Anthropic, one of the companies the guidelines address. Timothy Gowers, a member
  of the group, is the author of another selected work.
read: full
---

The Advisory Group on Mathematics and Artificial Intelligence has nine members: François Charles, Camillo De Lellis, Timothy Gowers, Martin Hairer, Nikhil Srivastava, Ulrike Tillmann, Ravi Vakil, Edward Witten and Melanie Matchett Wood. Its page says: "This group came together after OpenAI approached some of its members about establishing an external advisory board." The members chose to form an independent body instead, and they "do not accept payment for this work". These guidelines, published a week after the group announced itself, are its recommendations to any AI company whose models produce mathematics.

The document opens with a position that its recommendations do not depend on. Some companies test hard problems on models that no one else can use, and "we do not endorse this practice, and we ask them to stop testing advanced mathematical problems on proprietary models". The rest addresses what a company should do with results it has anyway.

A result that some mathematician fully understands should travel the usual way, through a preprint, peer review and talks. For output that no one understands, the people who prompted the model included, the group asks for five things at release:

- The company should search the literature for related ideas and cite them, and have a model rewrite each proof in the form of a conventional paper.
- Results should go to a scholarly repository that no AI company controls, with persistent identifiers and a record of changes.
- The company should publish "the name of the model, the prompts used, a (summarized) chain of thought, the time taken, and the estimated cost of computation".
- Proofs should be formalized where possible, and the formalization status stated where not.
- When many results are released together, a separate document should say "how many other problems of comparable difficulty the models tried and failed to solve, as well as how the problems were chosen".

The group adds: "We strongly recommend that AI labs refrain from treating the release of mathematical results as marketing vehicles to promote their models".

After release, a company that publishes mathematics no one understands "must take responsibility for ensuring that human understanding will follow". That means paying for workshops, working groups, postdoctoral positions and expository writing. Existing nonprofit institutions would decide what is funded, because the work of understanding "should not be directed by AI labs, even when the labs have produced the results". A last section asks companies to give mathematicians broad access to their public models and warns that research on private ones "risks creating a two-tier system where labs outrun the rest of the field".

The recommendations draw on a survey that received more than 600 replies and are described as "supported by a clear plurality of respondents". The document gives no figures from the survey and does not say how respondents were reached. A footnote says the survey "asked about a specific situation in which OpenAI announced the existence of many results without giving details". The guidelines are not binding. OpenAI released its collection of manuscripts a week later ({{openai-math-release}}), and the group wrote then that it had discussed the recommendations with the company and that "it is ultimately up to the mathematical community to assess the extent to which our recommendations were followed successfully".
