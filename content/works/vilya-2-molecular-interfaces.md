---
short: "Peptide interfaces"
title: Accurate structural modeling of chemically diverse molecular interfaces with Vilya-2
authors:
- Pascal Sturmfels
- Naozumi Hiranuma
- Milad Salem
- Benjamin D. Sellers
- Stephen Rettie
- CJ San Felipe
- Chase A. P. Wood
- Jeffrey K. Holden
- Adam P. Moyer
- Patrick J. Salveson
- Ivan Anishchanka
author_count: 11
org: Vilya
date: 2026-07-28
type: paper
url: https://arxiv.org/abs/2607.25156
links:
- kind: material
  label: 'Vilya: the Riptides benchmark of 88 protein-peptide complexes'
  url: https://github.com/VilyaPublic/Riptides
license: CC BY-NC-SA 4.0
beat: chemistry-medicine
edition: '001'
drafted_by: Claude Opus 5
well: D6
tier: notice
importance: Notable
novelty: New capability
evidence_type: Retrospective structure-recovery benchmarks against crystal and NMR structures, including
  a new benchmark assembled by the authors, with a co-folding model and a commercial docking program as
  baselines
evidence: Suggestive
independence: Self-reported by developer
read: full
checked:
- Preprint read in full, including the supplement
- Headline percentages checked against the paper's Table 1 and figures
- The version 1 date of July 28, 2026 and the license confirmed on arXiv
- The Riptides repository, the baseline runs and the internal campaign data were not examined
- No errors found in the text
coi: Every author works for the company whose model the paper evaluates. Four of the structures used to
  illustrate accuracy on marketed or clinical molecules are compared against co-crystal structures the
  company solved internally and has not released, or against structures of a progenitor compound.
found_via: The arXiv chemistry lens in the monitor's candidate file.
standfirst: Peptide drugs are built from non-standard amino acids and ring closures that co-folding models
  handle poorly. This model drops residue-level tokens and sequence alignments, treats every molecule
  as a graph of atoms and bonds, and recovers the bound shape of a peptide in about half of a new 88-complex
  benchmark.
---

Most structure-prediction networks represent a protein as a chain of residue tokens and everything else as atoms, and they use evolutionary information from sequence alignments. Peptide therapeutics fit that representation badly: they carry non-canonical residues, macrocyclization and stapling, and the drug candidates of interest bind pockets with no close analogue in the structural databases. Vilya-2 is a diffusion transformer built on the opposite convention. Its input is the chemical graph of the whole system (atomic number, hybridization, formal charge, bond order, aromaticity and stereochemistry), without residue tokens, molecule-type labels or alignments. Target and ligand are atoms in one graph. Instead of folding the whole protein, the model is conditioned on a sparse matrix of alpha-carbon distances taken from the target's reference structure and asked to model the local interface. The paper's justification is that most campaigns already know the fold and the epitope.

The paper's central number comes from Riptides, a benchmark the authors assembled and released: 88 protein-peptide complexes from structures deposited after June 2023, of which 51 are cyclic peptides with non-canonical chemistry. Sampling 100 poses and ranking them by the model's confidence, Vilya-2 recovers the bound peptide backbone within 2 Å in 54.1% of cases and within 1 Å in 38.0%; at 1,000 samples those rise to 59.1% and 40.9%. Boltz-2, run by the authors as the co-folding baseline and given the receptor's crystal coordinates as a template, reaches 40.9% and 22.7%. A commercial physics-based pipeline, MacroDock for macrocycles and Glide for linear peptides, reaches 22.0% and 15.9% on the 82 complexes where its docking succeeded. On small-molecule benchmarks the model reports 85.2% within 2 Å on PoseBusters and 79.5% on Runs N' Poses, with the gap to Boltz-2 widening as interfaces become less similar to anything in training: at the lowest similarity band the paper gives Vilya-2 above 60% and Boltz-2 at 20%. Training was restricted to Protein Data Bank entries released on or before September 30, 2021.

Repeated sampling helps: on peptide interfaces the success rate keeps rising out to 1,000 samples, where the paper reports that Boltz-2's ranking metric on these complexes is no better than random, so extra sampling cannot be converted into accuracy. The confidence score is also calibrated: a pose scoring above 0.8 has better than a 60% chance of being within 2 Å, which is what a design pipeline needs if it is to decide when to stop sampling. Applying the PoseBusters physical-validity filters before ranking, which is possible because those checks depend only on the chemical graph, leaves success rates unchanged while guaranteeing the top-ranked pose is physically valid.

The illustrations of accuracy on marketed and clinical molecules use unreleased, internally solved co-crystal structures for two of the four cases, and two others are compared against a structure of a progenitor compound. The activity work (fine-tuning the network to rank compounds by potency, where it reports a threefold enrichment of actives in the top fifth of its ranking against 1.3-fold for a fingerprint baseline and 1.9-fold for a message-passing network) uses measurements from a private hit-to-lead campaign, split chronologically to imitate prospective use. The miniprotein and large-molecule generalization results are retrospective recoveries of known NMR and crystal structures, scored as the best of thousands of samples; the supplementary table for the 21 disulfide-stapled miniproteins ranges from 0.39 Å to 4.21 Å.

No designed molecule in this paper was made or tested. What is measured is the step before that: whether the network picks the right bound shape, and whether its confidence means what it says. The authors call Vilya-2 "the structure-prediction oracle that de novo peptide design pipelines require". The test of that is a design campaign whose candidates the model chose, with the hit rate reported. {{cothinker-catalyst-selectivity}} fixed its predictions before the experiment.
