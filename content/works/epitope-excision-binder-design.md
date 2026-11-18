---
short: "Cropping the target saves compute"
title: Agent-guided epitope excision enables economical de novo binder design
authors:
- Jun W. Kim
- Artiom Myaskovsky
- Oscar Donosa
- Lawrence Chan
- Jameson K. Rogers
- Avinatan Hassidim
- Yossi Matias
- Annalisa Pawlosky
org: Google Research, Google DeepMind and Google Cloud
date: 2026-10-23
type: paper
url: https://arxiv.org/abs/2610.33195
license: CC BY 4.0
beat: life-sciences
edition: '004'
drafted_by: Claude Opus 5
well: C4
tier: notice
importance: Notable
novelty: New capability
evidence_type: A retrospective benchmark of 3,666 designs across 15 targets with known binding outcomes,
  one campaign on a new target run at three levels of agent autonomy under a fixed compute budget, and
  yeast-display screening of the resulting designs
evidence: Suggestive
independence: Self-reported by developer
read: partial
read_gap: The Methods section was read only in part, by searching it for the yeast-display protocol, the
  funding and the competing-interest statement; the five supporting figures and the supporting table were
  not read.
checked:
- Main text read in full, from the introduction through the discussion and its caveats
- Numbers quoted here checked against the paper's Table 1 and figure captions
- The version 1 date of October 23, 2026 and the license confirmed on arXiv; version 2 was posted on November
  15, 2026
- The arXiv record gives one author as Jameson K. Rogers and the paper's own author line gives Jamie Rogers
- No design was independently verified and no affinity was remeasured
- No errors found in the main text
coi: Six of the eight authors state that they are employees of Google and may hold Alphabet stock. Google
  is a direct competitor of Anthropic, which makes the drafting model.
found_via: The arXiv life-sciences lens in the monitor's candidate file.
standfirst: Refolding a designed binder against a 719-residue target wastes most of its compute on parts
  of the protein the binder never touches. Cutting the target down to a window around the intended interface
  reproduced the same interface geometry, cut structure-prediction time by about 88%, and let a language-model
  agent run the campaign; yeast display then recovered single-digit nanomolar binders.
---

A de novo binder campaign generates thousands of backbones, assigns sequences to them, and then refolds each candidate with its target to decide which few get made. The refolding step dominates the compute, and the cost is set by the whole target: AlphaFold3 pads its input to multiples of 256 tokens, so a complex with a 719-residue antigen lands in the 1,024-token bucket at about 59 seconds per fold while the binder touches a patch of a few dozen residues. Epitope excision keeps the contiguous sequence window spanning the binder's contacts plus a radial halo, discards the rest of the target, and folds against that. For the extracellular domain of fibroblast activation protein alpha, an 85 to 130-residue crop drops the complex into the smallest bucket, which the paper measures on an A100 as cuts of 89%, 66% and 88% in the time taken by backbone generation, sequence design and refolding.

The authors measure what the crop costs. Across 15 targets with known experimental outcomes and 3,666 designs, the excised crops reproduce the designed interface closely: median interface-core alpha-carbon deviation of 0.37 Å, with 93.7% of designs under 2 Å. Refolding the 394 confirmed binders against their intact targets for a design-by-design comparison gives the same median, 0.29 Å, in both conditions. Ranking suffers slightly: the mean average precision of the interface-confidence score falls from 0.47 on full targets to 0.40 on crops, driven by two targets with shallow alignments or fragile pockets. Dropping the target's multiple sequence alignment during refolding brings the crops back to within 0.012 of the full-target baseline, except on the SARS-CoV-2 receptor-binding domain, where the alignment holds the interface together and removing it halves ranking performance. There is also a floor on how small a crop can be: below about 85 retained residues, only 32% of confirmed binders refold within the 3 Å gate, against 97% between 85 and 200 residues. Seven of the 15 benchmark targets gain nothing at all, because their full complexes already fit the smallest bucket.

The second half compares how much of a campaign to hand to an agent. Against the same target, with the same hit definition and the same cap of 132.87 GPU-hours, three arms ran: the investigator alone, a hybrid in which Gemini 3.1 Pro chose epitope sets, crop sizes, design parameters and compute allocation while the investigator fixed the strategy, and a fully autonomous arm given only a strategy-neutral list of surface residues. The hybrid reached a 9.33% computational hit rate on 19,184 designs using 77.18 GPU-hours, against 5.06% on 33,024 designs for the investigator alone, and 23.2 hits per GPU-hour against 12.6. The autonomous arm reached 6.18%, stopped itself at 94% of the budget, and spread its designs over 13 distinct epitopes against 7 for the hybrid and 4 for the investigator. Left to choose, it opened by proposing to occlude the mouth of the catalytic channel and filtered candidate hotspots by solvent exposure, crystallographic order and distance to the catalytic triad, which the paper describes as "effectively piecing together the same buildability criteria used by human designers without being prompted with those rules".

A fourth arm, identical in autonomy to the hybrid, changed two scoring settings (target alignment off, the more conservative confidence direction as the ruler) and appeared to reach 32.62% on the frozen metric, or 19.31% on its own. The authors exclude it from the autonomy comparison and report it as a control on the apparatus.

Designs from all four arms went into a 5,000-member yeast-display library, 1,250 per arm, screened over three rounds of sorting at falling antigen concentrations. Sequencing found 327 sequences identical to a design enriched, along with about 5,000 within 14 residues of one; the exact designs gained read depth far faster, from a mean of 3 reads to 547 across rounds, against 1.3 to 9.6 for the related sequences. The two arms whose designs were most enriched were the autonomous arm and the apparatus-ablated variant, with 105 exact designs each, against 67 for the hybrid and 50 for the investigator, an ordering that does not match the computational hit rates the autonomy comparison was built on. Four representative clones gave apparent dissociation constants of 3.0 to 9.1 nM.

Excision is tested across 15 targets and thousands of designs with known outcomes; the autonomy ladder is one target, one backbone class, one controller and one trajectory per arm, which the authors state, along with the possibility that an agent policy tuned to exhaust its budget would have found more. The wet-lab result establishes that the pipeline produces real binders against a large enzyme. No affinity comparison between arms is reported, and binding was measured on the yeast surface, with characterization of soluble binders and of inhibition left to future work. The engineering claim the paper opens with holds: the compute spent on the rest of the target can be reclaimed without moving the interface.
