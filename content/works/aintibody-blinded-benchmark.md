---
short: "AIntibody benchmark"
title: A blinded, prospective benchmark of in silico antibody discovery anchored to experimental affinity and developability
authors:
- M. Frank Erasmus
- Daniel Bedinger
- Elizabeth Hopkins
- Ginger Ferguson
- Justine Strickler
- Christilyn P. Graff
- Samantha R. Summers
- Stacy L. Capehart
- Joshua D. Slocum
- Crystal Richardson
author_count: 117
org: Specifica, an IQVIA business, with the participating organizations of the AIntibody challenge
date: 2026-08-19
type: paper
url: https://www.nature.com/articles/s41587-026-03238-6
links:
- kind: context
  label: 'Specifica and the AIntibody consortium: the challenge''s own site'
  url: https://www.aintibody.org/
- kind: response
  label: 'Derek Lowe: commentary on the challenge results'
  url: https://www.science.org/content/blog-post/state-ai-antibody-design
- kind: response
  label: 'In the Pipeline feed: the text of Lowe''s post'
  url: https://www.science.org/blogs/pipeline/feed
license: CC BY 4.0
beat: life-sciences
edition: '002'
drafted_by: Claude Opus 5
well: C4
tier: lead
importance: Major
novelty: New evidence
evidence_type: Prospective blinded challenge; every submitted antibody expressed as an IgG and measured
  by surface plasmon resonance, a kinetic exclusion assay and a five-assay developability panel
evidence: Solid
independence: Peer-reviewed
read: full
checked:
- Article read in full on the journal page
- Headline figures checked against the source text
- License, publication date, affiliations and competing-interest statement confirmed on the journal page
- No errors found in the main text beyond two internally inconsistent figures
- Supplementary data and notes not examined
coi: The challenge was organized by Specifica, whose staff are also the first and last authors, and most
  of the participating organizations are co-authors on the paper that ranks their own submissions.
found_via: The monitor's feeds carried Derek Lowe's post about the challenge; the paper itself was found
  by web search. Nature Biotechnology is not on the monitor's source list.
standfirst: Twenty-nine organizations submitted 511 designed or predicted antibodies against the SARS-CoV-2
  receptor-binding domain, and the organizers made and measured every one. The best design matched the
  best antibody from the laboratory, and on the ranking task all but one method did worse than picking
  clones at random.
claims:
- claim: In affinity maturation, the best AI-designed antibody reached 95 pM by kinetic exclusion assay,
    against 113 pM for the best experimentally derived antibody, and the two are statistically indistinguishable.
  status: supported
  note: Measured by the organizers under a uniform protocol. The confidence intervals overlap (67.7 to
    178 pM for the experimental antibody, 69.1 to 127 pM for the design). The Discussion gives the design
    as 94.7 pM.
- claim: On the task of picking the highest-affinity clone from a sequenced cluster, all but one method
    did worse than random clone picking.
  status: supported
  note: Between 9.8% and 13.8% of submissions beat the most abundant clone, against 39% for randomly picked
    clones. Only one group, the Fremont laboratory at Washington University, exceeded that baseline, at
    50%, and it failed on one of the three clusters.
- claim: A consensus sequence derived from the selection data, with no machine learning, ranked third in
    the affinity-maturation challenge.
  status: supported
  note: ProBioGen's submission matched the library consensus at all six complementarity-determining regions
    and scored zero on the developability panel. The paper gives it as 540 pM in the Results and 538 pM
    in the Discussion.
- claim: The antibody that won the out-of-library design task on affinity, at 2.9 pM, would probably not
    be developable.
  status: supported
  note: It failed to elute from the hydrophobic-interaction column and showed cooperative binding with
    a Hill coefficient of 1.41. The composite score let one failure be offset elsewhere, which the authors
    identify as a limitation of their own scoring.
- claim: No method generalized across tasks.
  status: supported
  note: Every disclosed group had at least one challenge in which its best submission fell well outside
    the leaders.
---

AIntibody is a prospective, blinded challenge modeled on the Critical Assessment of Structure Prediction. Participants were given deep sequencing data from antibody selection campaigns against the SARS-CoV-2 receptor-binding domain and set three tasks: mature a parental antibody in silico by redesigning five of its six complementarity-determining regions; identify the highest-affinity developable sequence within each of three clusters defined by a shared heavy-chain CDR3; and design antibodies that do not appear in the provided data by changing CDRs but not frameworks. Twenty-nine organizations submitted 511 sequences, which the organizers expressed as full IgGs and measured by high-throughput surface plasmon resonance, by a kinetic exclusion assay for the strongest binders, and on five developability assays scored and summed into a composite. The authors write: "Experimentally validated prospective, blinded benchmarks are needed to separate durable advances from hype in computational antibody design".

In the affinity-maturation task, 25 organizations submitted 165 sequences. Of these, 118 (71.5%) bound the target and 47 did not; 22 reached single-digit nanomolar affinity, five were subnanomolar and one was below 100 pM. The best design measured 340 pM by surface plasmon resonance against 517 pM for the best antibody from the experimental campaign, and 95 pM by kinetic exclusion assay against 113 pM. Eight of the 25 participants produced no developable binder at all. The design that ranked third, from ProBioGen, was the most common residue at each position of each sublibrary, which the authors report as "demonstrating that statistical analysis of the selection data, without machine learning (ML), was sufficient to produce one of the top-performing designs in challenge 1".

The ranking task went worse. Between 9.8% and 13.8% of submissions improved on the simple heuristic of taking the most abundant clone in a cluster, against 39% for clones picked at random. "It is notable that all but one of the AI prediction strategies were worse than random picking at identifying high-affinity binders", the authors write, and "For most participants, using their AI models to select antibodies was actively counterproductive relative to the baseline strategy of selecting the most abundant clone and picking additional random clones." Developability tracked the heavy-chain CDR3 cluster: every antibody in one cluster passed, while 41.4% of submissions in another were disqualified.

In the out-of-library task, 23 organizations submitted 168 sequences, of which 51 (30.4%) did not bind. Two designs were tighter than the best experimental antibody, at 2.9 and 3.1 pM against 9.2 pM. The 2.9 pM winner failed to elute from the hydrophobic-interaction column, a flaw the authors say "would have probably doomed it as a clinical candidate"; the next developable design, at 8.69 pM, was statistically tied with the experimental antibody. Winning designs stayed close to the provided data, reusing a heavy-chain CDR3 from the dataset and changing one to five residues elsewhere.

The target was chosen to make success likely, and the second and third tasks supplied measured affinities that are not normally available at the equivalent stage: "The results presented here should be interpreted as an upper bound on current computational capability for this target class, not as evidence of general-purpose performance across arbitrary antigens or data regimes." The authors also note that "AIntibody's first iteration evaluated a single antigen, was organized by the same consortium now reporting the results and relied on organizer integrity rather than informatic safeguards for blinding". The paper dates the picture it gives of the field "as of Q1 of 2025".

The organizers and most participants are co-authors, and the competing-interest statement lists employment at more than twenty companies whose methods were ranked. The measurements, however, were made centrally by three vendors under one protocol, and the comparison is against experimental antibodies from the same campaigns. Two figures are internally inconsistent: the winning affinity-maturation design appears as 95 pM in the Results and 94.7 pM in the Discussion, and the ProBioGen consensus design as 540 pM and 538 pM.

Writing in *Science*'s In the Pipeline, Derek Lowe responded: "I'm sticking to my contention that antibody development is the best AI case right now. And that, folks, is because all the others are even harder than this!"
