---
short: "One matrix multiply"
title: 'Accuracy is not compatibility: two Evo 2 checkpoints hinge on one FP8 matrix multiplication'
authors:
- Xun Ding
- Ziyuan Qin
org: An independent researcher and Emory University
date: 2026-10-29
type: paper
url: https://arxiv.org/abs/2610.39415
links:
- kind: material
  label: 'The authors: mmaemu, the FP8 matrix-multiplication emulator, with validation logs'
  url: https://github.com/astding/mmaemu
- kind: material
  label: 'The authors: the deposited runs, per-variant scores and manifests'
  url: https://doi.org/10.5281/zenodo.23740390
- kind: context
  label: 'Arc Institute and collaborators: the Evo 2 model whose checkpoints are tested'
  url: https://github.com/ArcInstitute/evo2
license: arXiv.org perpetual non-exclusive license
beat: life-sciences
edition: '004'
drafted_by: Claude Opus 5
well: C5
tier: notice
importance: Notable
novelty: Audit or replication
evidence_type: Controlled substitution of one matrix multiplication at a time on fixed weights, using
  an emulator validated bit-for-bit against captured outputs, scored on the developers' own tests and
  on a variant-classification task
evidence: Solid
independence: Independent
read: full
checked:
- Preprint read in full, including the limitations, methods, availability, funding and competing-interest
  statements
- Losses, accuracies and areas under the curve checked against the paper's Table 1 and figures
- The version 1 date of October 29, 2026 and the license confirmed on arXiv
- The deposited data and the emulator were not downloaded or run, and no experiment was repeated
- No errors found in the text
coi: The authors declare no competing interests and no funding, and state that they paid for GPU rental
  themselves. They also state that Anthropic's Claude and OpenAI's Codex assisted with the code, the experiments,
  the analysis, the figures and the drafting; the drafting model here is Anthropic's.
found_via: The arXiv life-sciences lens in the monitor's candidate file, where it scored zero on keywords.
standfirst: A DNA language model's published weights stop working when the hardware adds up its 8-bit products
  more accurately. On a consumer Blackwell card the 40-billion-parameter checkpoint predicted the next
  base no better than chance and scored BRCA1 variants at an area under the curve of 0.434; restoring
  one matrix multiplication out of 42, with the weights untouched, brought it back to 0.869.
---

The 8-bit floating-point specification says how numbers are stored and leaves out how products are summed. Different tensor cores keep different numbers of bits while accumulating, and libraries differ in how they split and recombine partial sums. The paper's observation is that a released checkpoint can depend on those choices: "FP8 formats specify how values are stored, not how products are summed; this gap can break checkpoints."

Evo 2 documents a Hopper requirement for three of its checkpoints. On two Blackwell cards, the 1-billion and 40-billion-parameter checkpoints fail the developers' forward test while the 7-billion passes. On one card the 40B's mean next-base cross-entropy came out at 1.4023 against an expected 0.2159, and it predicted the next base correctly 25.7% of the time, where guessing among four bases gives 25%. At the first projection of the 1B on one test window, the newer card returned the correctly rounded value for 99.996% of outputs, against about 30% on either reference GPU, whose results are biased toward zero in the manner of truncating accumulation. Accumulating the same 8-bit operands in 32-bit floating point, with no FP8 kernel involved, reproduces the failure.

To locate the dependence the authors built an emulator of the reference platforms' matrix multiplications, validated bit-for-bit against 168 captured outputs, and then swapped the arithmetic of one projection at a time while the executing GPU, the weights and the operands stayed fixed. In the 1B, computing block 0's projection (the first of 21) the old way and leaving the other 20 native passes the test; doing the reverse fails. In the 40B, which has 42 projections, the same one is enough: with block 0 restored from a lookup table and everything else native, the forward loss lands 0.0011 from the expected value against a tolerance of 0.001, a near miss, while variant classification recovers almost entirely.

Following the model's notebook, the authors scored 500 BRCA1 variants, 111 of them loss-of-function in a genome-editing assay, by the change in sequence likelihood. The 40B gives an area under the curve of 0.868 on an H100 and 0.434 natively on the consumer card, below chance, with per-variant scores essentially uncorrelated with the reference. Restoring one projection raises it to 0.869, a paired difference of 0.435, with a per-variant correlation of 0.997 against the reference. On a server-class Blackwell card under a different software stack the same substitution moved the 40B from 0.481 to 0.867 and the 1B from 0.556 to 0.721. A user who ran the published weights on the wrong card without checking would have produced variant rankings that are noise.

The explanation is narrower than "less precision is better". Exact accumulation at that projection fails; the exact sum multiplied by the reference GPU's measured 1.4% shrinkage toward zero passes; the reference chain with that shrinkage divided back out fails; 13-bit truncation rounded to nearest instead of toward zero fails; of nine sampled gains only two passed, and two gains equidistant from the exact value behaved differently depending on direction. Injecting random perturbations matched in size to the native-versus-reference difference at the same point in the network left the model working, while the structured difference collapsed it. The authors offer a mechanism by which training could have produced such a dependence, label it a candidate explanation only, and write that establishing it would require controlled training runs they did not do.

The paper covers one model family, two consumer-and-workstation Blackwell cards, no 20B or B200 or B300 runs, one assay and one 500-variant cohort, with an in-sample gain estimate and a follow-up that changed software as well as hardware. The two reference GPUs differ on every captured projection, yet both support the expected behavior, and they agree on the sign of only 84.2% of the 1B's variant effects, so cross-platform variation is a measurable floor under small score differences. The recommendations follow from that: "determinism is not compatibility"; releases should publish reference outputs for applications along with tolerances, the GPU configuration and the effective accumulation mode; and a cheap screen, rerunning a model's tests with the same operands accumulated in 32-bit, may reveal the same class of dependence elsewhere, untested so far beyond this model.
