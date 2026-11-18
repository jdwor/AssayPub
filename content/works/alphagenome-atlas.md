---
short: "DeepMind predicts every DNA change"
title: 'AlphaGenome Atlas: a high-resolution map of human DNA'
authors:
- Pushmeet Kohli
- Žiga Avsec
org: Google DeepMind
date: 2026-09-08
type: dataset
url: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/
links:
- kind: material
  label: 'Google DeepMind: the same announcement on the DeepMind blog, with further detail'
  url: https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/
license: ''
beat: life-sciences
edition: '003'
drafted_by: Claude Opus 5
well: C3
tier: lead
importance: Notable
novelty: New resource
evidence_type: Precomputed model predictions, with three collaborator case studies described in the announcements
evidence: Suggestive
independence: Self-reported by developer
read: full
checked:
- Both announcement posts read in full
- Figures and quotations checked against those posts
- The accompanying paper, the web portal and the API were not opened, and no prediction was checked
- The portal's terms of use could not be confirmed from a primary page; only the two announcements' description
  of them is used here
coi: The drafting model is made by Anthropic, a competitor of Google DeepMind.
found_via: Named by the editor. The monitor's Google feeds did not return it.
standfirst: Google DeepMind ran its AlphaGenome model over every possible single-letter change in the human
  genome and released the results as a one-petabyte database, free for academic use, with a single combined
  score per variant. The entries are predictions, and the evidence for them is three collaborations that
  Google DeepMind describes.
claims:
- claim: The Atlas holds predicted molecular effects for every possible single-nucleotide variant in the
    human genome, about 9 billion of them, released as a 1-petabyte dataset.
  status: self-reported
  note: The scale is stated in both announcements. Nothing in them can be checked against an outside source,
    and no prediction was verified here.
- claim: The release's combined score outperforms existing methods on variant pathogenicity and rare-disease
    benchmarks.
  status: self-reported
  note: Neither announcement names a benchmark, metric or comparison method behind the statement that
    the score "provides best-in-class performance across many variant pathogenicity and rare disease benchmarks".
    Both link an accompanying paper that was not opened.
- claim: Grouping rare non-coding variants by their predicted molecular effect found 22% more non-coding
    genetic associations in whole-genome data from more than 54,000 UK Biobank participants.
  status: self-reported
  note: Attributed to Gareth Hawkes at the University of Exeter but reported by Google DeepMind, with
    no paper or preprint cited in the announcements.
- claim: Re-ranking variants with the score solved a rare-disease case, identifying a variant in DNM1 predicted
    to create an incorrect splice site, which experimental screens then confirmed.
  status: self-reported
  note: One variant in one case, from a collaboration with the GREGoR Consortium and the Broad Institute.
    The experimental validation is asserted in the announcements; no data, assay or report is given.
- claim: Access is free for academic research, through a web portal that needs no coding, an API and an
    agent skill.
  status: unverified
  note: The announcements state this, and the portal and its terms of use were not opened, so no access
    condition beyond that description is established.
---

AlphaGenome predicts molecular consequences of changes in DNA sequence, including effects in the non-coding genome. AlphaGenome Atlas is the model's output run ahead of time over the whole human genome: Google DeepMind describes it as "a database that predicts the effects of every possible single nucleotide variant in the human genome", about 9 billion of them, held as a 1-petabyte dataset. For each variant the Atlas holds thousands of molecular-effect predictions across human and mouse cell types, together with a new summary number, the AlphaGenome Variant Impact score, which merges AlphaGenome's regulatory predictions with AlphaMissense's protein-level predictions. The score is broken into contributions from categories such as chromatin accessibility, splicing and conservation, and the release includes a catalogue of more than 2,500 recurrent sequence motifs. Access is through a web portal that needs no coding, through the AlphaGenome API, and as a skill in Google Antigravity; the portal is described as free for academic research.

With the GREGoR Consortium, Laura Covill, Anne O'Donnell-Luria and colleagues at the Broad Institute used the score to re-rank variants in unsolved rare-disease cases and found one in *DNM1*, predicted to create an incorrect splice site; DeepMind says experimental screens validated the prediction. Gareth Hawkes at the University of Exeter applied the Atlas to whole-genome data from more than 54,000 UK Biobank participants and, by grouping rare variants by predicted molecular effect, "uncovered 22% more non-coding genetic associations"; restricting attention to the 1% of non-coding variants predicted to be most impactful, he identified 19 regions associated with body mass index. Julia Zeitlinger and Melanie Weilert at the Stowers Institute used the motif catalogue to separate transcription factors that change DNA accessibility from those that also switch genes on and off.

The headline numbers describe scale. On accuracy the company says only that "Our testing shows that the AVI score provides best-in-class performance across many variant pathogenicity and rare disease benchmarks", without naming the benchmarks or the comparison methods in either announcement, though both link a paper that would contain them. The collaborator results come from DeepMind's announcements, and the rare-disease case is a single variant. A predicted molecular effect is not a clinical interpretation. DeepMind writes that it views the Atlas "as a baseline rather than an endpoint".
