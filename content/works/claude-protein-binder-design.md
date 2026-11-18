---
short: "1,440 binders measured"
title: Claude protein binder design (data release v1.0)
authors:
- Anthropic
org: Anthropic, with Adaptyv Bio and Twist Bioscience
date: 2026-08-17
type: dataset
url: https://huggingface.co/datasets/Anthropic/claude-protein-binder-design
links:
- kind: material
  label: 'Anthropic: the data release''s own README, with the assay formats and headline counts'
  url: https://huggingface.co/datasets/Anthropic/claude-protein-binder-design/raw/main/data/README.md
- kind: material
  label: 'Anthropic: the data notes, listing the caveats that bear on every number'
  url: https://huggingface.co/datasets/Anthropic/claude-protein-binder-design/raw/main/data/docs/DATA_NOTES.md
license: CC BY 4.0
beat: life-sciences
edition: '002'
drafted_by: Claude Opus 5
well: C2
tier: notice
importance: Notable
novelty: New resource
evidence_type: Every design expressed and measured at two contract research organizations in different
  assay formats, with raw traces, vendor fits, replicates, controls and per-design provenance released
evidence: Solid
independence: Independent
read: partial
read_gap: The dataset card, the data release's README and the data notes were read; WETLAB.md, INSILICO.md,
  PROVENANCE.md and LOOKUP_TABLES.md, the twenty Parquet tables, the per-design folders, the 74.5 GB structure
  and PAE release and the 1.16 GB prompts release were not opened, so the rubric behind the final binder
  calls and the per-target statistics are described here as the documentation describes them.
checked:
- The dataset card, the data release README and the data notes read in full
- Counts, vendor totals and agreement figures checked against those documents
- The August 17, 2026 creation date and the CC BY 4.0 license confirmed from the repository's metadata
  record
- The measurements themselves were not recomputed and no design was independently verified
- No errors found in the documentation; the vendor and final counts in it are mutually consistent
coi: The designs, the campaigns and the release are Anthropic's, the designing agents were two Claude
  models, the final binder call for every design was made by Claude under a fixed rubric, and the drafting
  model is also Anthropic's. The measurements were made by two outside vendors under contract.
found_via: The monitor's Hugging Face source list.
standfirst: Two Claude models were run as protein-design agents against 16 targets, and all 1,440 designs
  were sent out for expression and binding measurement at two contract research organizations in different
  assay formats. The raw traces, the disagreements between the two vendors and the rule used to settle
  them are all in the release.
---

The release holds 1,440 de novo miniproteins of 50 to 120 residues, designed against 16 targets by two models acting as autonomous design agents: 900 from Mythos Preview, across single-target campaigns on all 16 targets and a multi-target campaign on 14, and 540 from Opus 4.8, across a multi-target campaign and four single-target sets. The targets mix receptors and signaling proteins with awkward cases: SpCas9, a de novo protein, a viral Bcl-2 homolog, bacterial maltose-binding protein, two forms of GDF-8. Each design ships with its design model, the best of five seeds from each of ten co-folding predictors, and a provenance record of how the agent produced it, and the campaign prompts and the corpus of documents the agents were given are released separately.

The measurement was contracted out twice, in formats that fail differently. Adaptyv Bio expressed each design cell-free and immobilized it as a monovalent ligand, flowing the antigen over it: 2,467 surface plasmon resonance replicates and 345 by biolayer interferometry. Twist Bioscience cloned each design as a human IgG1 Fc fusion, expressed it in Expi293 cells and captured it on an anti-Fc surface, so its ligand is bivalent, then ran six-point antigen titrations with orthologs and negative controls alongside, plus expression titer and analytical size-exclusion chromatography. Adaptyv returned a binding call for 1,296 designs and called 336 of them binders. Twist measured 1,254 and found a kinetic fit on the human antigen for 325, of which 272 passed its quality control.

The two vendors disagree often. Of the 1,235 designs with a result from both, 253 bind at both, 846 at neither, 69 at Adaptyv only and 67 at Twist only, which the documentation gives as 89.0% agreement while noting that the agreement is dominated by the joint negatives. The released count of successes, 354 binders out of the 1,320 designs with interpretable wet-lab data, came from Claude, which reviewed both vendors' evidence (reported calls, sensorgram shape, a standardized re-fit, replicate consistency, expression and capture levels, control behavior) and encoded its judgment as a fixed rubric applied identically to every design, then checked each call against the raw traces, which changed 29 of them. The documentation says of that step: "The assessment is a rubric, not a new measurement", and "It supplements the vendor calls and never replaces them".

Several of the documented caveats bear on the affinities. Seven of the sixteen antigens are oligomers or complexes, so 1:1 fits give apparent affinities that can include avidity, most strongly in the bivalent Twist format; 420 designs carry that flag, and the notes say to read sub-nanomolar values on those targets accordingly. The antigen differs between vendors for three targets: free RBX1 at one and a CUL1-RBX1 complex at the other, where part of the surface is occluded; Cas9 as a ribonucleoprotein at one and also as the apo protein at the other, where ten designs are hits only on the apo form. Nineteen designs fit an unrelated negative-control antigen. The 120 designs against mature GDF-8 have no usable measurement, because the antigen aggregated and bound the assay surfaces non-specifically at both vendors, and they are excluded from every count. Ortholog antigens were run only where an ortholog was meaningful and available, so cross-reactivity is untested for hundreds of designs, which the notes mark as a coverage gap.

Success is also very uneven across targets: maltose-binding protein has no binder among 90 designs at one vendor and one hit at the other, and the de novo target BBF-14 and the enzyme 15-PGDH have one each. On two targets a positive control failed: at Adaptyv the TrkA control did not express, and the IL-7Rα control expressed but did not bind. Those plates lack the reference they were meant to have. The in-silico scores the agents used to choose designs are released with a caveat: the summary confidence for each design is the maximum over five seeds, which the notes say is optimistic relative to single-seed thresholds and comparable only within one predictor, target and stoichiometry.

A reader who distrusts the model-adjudicated 354 can work from either vendor's calls, or from the 253 designs both vendors scored as binders, because the traces and fits are there. {{aintibody-blinded-benchmark}}, published two days later, had designs from many groups measured centrally by an organizer with no stake in which method won.
