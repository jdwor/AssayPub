---
short: "Redesigned starting points"
title: AI-redesigned starting points and outcomes enhance protein evolution
authors:
- Nicholas A. Krasnow
- Joy A. Xu
- Emily Zhang
- Gandhar K. Mahadeshwar
- Y. Allen Tao
- Julia McCreary
- Colin F. Hemez
- Logan E. Brown
- Wei Jiang
- David R. Liu
author_count: 10
org: Broad Institute of Harvard and MIT, Harvard University and the Howard Hughes Medical Institute
date: 2026-07-22
type: paper
url: https://www.nature.com/articles/s41586-026-10820-0
links:
- kind: material
  label: 'Nicholas Krasnow: the sequence-design procedure used for the proteases'
  url: https://github.com/Nicholas-Krasnow/sequence-design-guide
- kind: material
  label: 'Nicholas Krasnow: the long-read sequencing analysis'
  url: https://github.com/Nicholas-Krasnow/LoopSeq
- kind: context
  label: 'Europe PMC: the record for this paper, with no earlier version'
  url: https://europepmc.org/article/MED/42486980
license: CC BY 4.0
beat: life-sciences
edition: '001'
drafted_by: Claude Opus 5
well: C3
tier: lead
importance: Major
novelty: New evidence
evidence_type: Replicate side-by-side continuous-evolution campaigns from redesigned and wild-type starting
  points, with each campaign's evolved mutations grafted into the other background and measured
evidence: Solid
independence: Peer-reviewed
read: full
checked:
- Article read in full on the journal page, including methods, funding and competing-interest statements
- Quotations and figures checked against the article text
- Open-access license, the July 22, 2026 publication date and the author list confirmed on the journal page
- Europe PMC searched for an earlier version of the paper; the Nature article is the only record
- Supplementary tables, notes and the peer-review file were not opened
- No errors found in the text
coi: Two authors are inventors on patent applications filed by the Broad Institute on this work, and
  the corresponding author is a cofounder, consultant or equity holder in five companies, which the paper
  lists.
found_via: Web search. Nature's table of contents is not on the monitor's source list.
standfirst: ProteinMPNN was used to rewrite the stable core of three botulinum neurotoxin proteases while
  leaving their active sites fixed, and the redesigned enzymes were then put through continuous evolution
  beside the natural enzymes in the same selections. The redesigned starting points reached higher activity
  in every campaign, and in several cases they tolerated mutations that destroyed the natural enzyme.
claims:
- claim: Across four evolution campaigns, proteases evolved from redesigned starting points reached higher
    activity than proteases evolved from the corresponding wild-type enzyme in the same selection.
  status: supported
  note: Measured as luciferase-reported activation of the selection circuit by consensus clones. On the
    least difficult substrate the redesign-evolved enzymes gave 6.1 to 7.7-fold activation against 2.6
    to 3.0-fold for the wild-type-evolved enzymes; on the hardest, 16 and 20-fold against 10-fold. The
    authors ran all the assays.
- claim: The redesigned background supports mutations that do not work in the wild-type enzyme, and the
    reverse is not true.
  status: supported
  note: K225E, which appeared in both successful campaigns on the hardest substrate from the redesigned
    start, conferred no activity when grafted into the wild-type protease; it lowers the melting temperature
    of the wild-type enzyme to 45 °C. Wild-type-evolved mutations, by contrast, generally worked when
    grafted into the redesigned backgrounds.
- claim: On the hardest substrate, two of four replicate campaigns from the wild-type protease failed
    to evolve any activity before phage washout, while all four from the redesigned protease succeeded.
  status: supported
  note: One substrate, one protease family and four replicates per starting point, run on automated continuous-culture
    devices.
- claim: A protease evolved from a redesigned starting point cleaves the therapeutic target ataxin-2 with
    more than 79-fold greater selected specificity than the best protease evolved from the wild-type enzyme.
  status: supported
  note: The results section gives the two best design-evolved proteases as having "79-fold and more than
    56-fold greater selected specificity" than the best wild-type-evolved enzyme, and the abstract gives
    the figure as more than 79-fold; both are bounded by the detection limit of the off-target assay. No cleavage of the native substrate was detected for one of them even at
    super-stoichiometric protease concentrations.
- claim: Redesign also repaired a protease that earlier evolution had destabilized, without undoing its
    reprogrammed specificity.
  status: supported
  note: Grafting the 16 evolved mutations of a PTEN-cleaving variant into three redesigned backgrounds
    raised soluble expression in E. coli by 2.2 to 5.2-fold and expression in human cells by more than
    24-fold, with activity on the original substrate still undetected.
---

Directed evolution usually starts from a natural protein, and natural proteins are only marginally stable. Mutations that confer a new activity are frequently destabilizing, so an evolving enzyme uses up its stability margin to gain function and often ends with lower activity on its new substrate than the parent had on its old one. Here that margin is enlarged before evolution begins. ProteinMPNN was given the predicted structure of a botulinum neurotoxin protease with the substrate pocket, the zinc site and conserved positions held fixed, and asked to rewrite the rest; the resulting variants were screened for folding in silico and then expressed and assayed. Of 74 designs of BoNT/E protease, 58 were functional proteases, 33 cleaved at least as fast as the wild type, and 22 both kept activity and expressed better. Three of these, the ones carried forward, had catalytic efficiencies of 190 to 310 mM⁻¹ s⁻¹ against 110 mM⁻¹ s⁻¹ for the wild type, and higher melting temperatures. The same procedure worked on two other serotypes, and a physics-based method, PROSS, produced comparable variants with fewer and more conservative mutations.

Three substrate variants of increasing difficulty were chosen by profiling the protease against all 441 single-residue variants of its native substrate. Each substrate was then evolved from the redesigned enzyme and from the wild type in three or four replicate lagoons apiece, under identical flow schedules, using phage-assisted continuous evolution on automated culture devices; 44 independent evolutions were run in all. Every consensus genotype was then grafted into the other starting point, which separates two explanations for a difference in outcome: a better starting point, or evolutionary luck.

The grafts came out asymmetric. Redesigned backgrounds accepted most mutations found from the wild-type start, and did at least as well with them. Wild-type backgrounds frequently did not work with mutations found from the redesigned start: on the easiest substrate, no redesign-evolved genotype was functional in the wild-type enzyme. The paper traces this to stability. K225E, which arose in both successful redesign campaigns on the hardest substrate, lowers the melting temperature by 4.3 °C in the wild-type enzyme and 6.5 °C in the redesign, leaving the wild type at 45 °C and the redesign at 48 °C, and its melting transition in the wild-type background spreads over a wider range. Long-read sequencing of whole populations shows the same pattern over time: wild-type lagoons drifted to more distant, multiply mutated genotypes, while redesign lagoons kept single mutants to the end. Where the redesign could reach high activity with one base change and the wild type needed two to four, the redesign adapted in less time.

A fourth redesign, D4, separates stability from activity. D4 cleaves its substrate 20-fold more slowly than the wild type but melts at a higher temperature, and the enzymes evolved from it were as active as those evolved from the better-balanced redesigns. Plotting evolved and grafted genotypes in a protein language model's embedding space, the authors describe the wild-type landscape as sparse, with its few functional solutions far from the starting sequence, and each redesign as raising the average level of the landscape and adding functional sequences both near and far.

The application is a protease retargeted to ataxin-2, a protein implicated in neurodegeneration, with the native substrate selected against at the same time. The best enzyme evolved from a redesigned start carries 46 mutations from ProteinMPNN and 18 from evolution, 16% different from the natural protease, against 2.4% for the best wild-type-evolved enzyme. It cleaves ataxin-2 1.7-fold faster than the best wild-type-evolved protease, shows no detected cleavage of the native substrate, is less toxic to human cells, and produces the cleavage product more efficiently on co-transfection. Grafting its evolved mutations into the wild-type enzyme gave no ataxin-2 activity at all, which is the paper's explanation for why that genotype never appeared in the wild-type lagoons.

The work covers one protein family and one selection system, with substrates reached from a single native specificity, and the laboratory that designed the enzymes made all the measurements. The authors write that the generality of "the consistent superiority of evolutionary outcomes from redesigned proteases observed in this study" to other proteins "will require future investigations". The final enzymes show the cost of the approach: the ataxin-2 proteases evolved from the redesign are strongly destabilized relative to their starting point, and end up only somewhat more stable than the wild-type enzyme they started above.
