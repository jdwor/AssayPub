---
short: Markets for scarce experiments
title: Agentic Economies for Autonomous Scientific Discovery
authors:
- Nenad Tomasev
- Matija Franklin
- Atoosa Kasirzadeh
- Vivek Natarajan
- Alan Karthikesalingam
- Sebastien Krier
- Simon Osindero
org: Google DeepMind
date: 2026-09-25
type: paper
url: https://arxiv.org/abs/2609.31562
links:
- kind: material
  label: PDF
  url: https://arxiv.org/pdf/2609.31562
license: CC BY 4.0
beat: autonomous-discovery
edition: '003'
well: A4
tier: lead
importance: Notable
novelty: New framing
evidence: Not applicable
evidence_type: Position paper based on existing literature; no new data
independence: Self-reported by developer
checked:
- Read in full except section 6.1
- Quotations checked against the source
- License and dates confirmed on arXiv
coi: All seven authors work at Google DeepMind, which builds research agents. The paper says its views are personal.
found_via: Named by the editor. Also returned by the arXiv monitor (autonomous-discovery and general lenses).
standfirst: Seven Google DeepMind researchers argue that when AI systems can generate hypotheses cheaply, the limiting
  resource is the capacity to test them. They propose markets and institutions for allocating that capacity among
  AI agents and laboratories. The paper presents no new data.
claims:
- claim: Autonomous science is likely to be limited mainly by physical resources and empirical validation rather
    than by the supply of plausible ideas.
  status: unverified
  note: A forecast argued from the literature. It is consistent with a Google survey in which scientists report
    a growing backlog of untested hypotheses ({{ai-in-science-early-insights}}).
- claim: A four-stage "Hypothesis Exchange Pipeline" could register, price, broker and reward machine-generated
    hypotheses.
  status: unverified
  note: A proposal that has not been built or tested.
- claim: Ideas could be rewarded retroactively in proportion to their eventual impact.
  status: unverified
  note: 'Requires an objective measure of an idea''s impact. The authors write: "At the moment, we lack this capability."'
read: partial
read_gap: Section 6.1, on dual-use research and biological risk, was not read. The drafting model is restricted
  on that subject.
---

This is a position paper. Its starting point is that AI systems can produce plausible hypotheses at low cost while experiments remain slow and expensive. The authors conclude that autonomous discovery "becomes primarily a problem of multi-agent coordination and collaboration over scarce resources", and they treat the allocation of instruments, data and computing as a problem in market design.

The second section sets out why validation is slow. Drug development costs have risen for decades, clinical trials are limited by the supply of volunteers and by the time a disease takes to progress, crop trials wait on growing seasons, and large instruments are few. Observational data and simulations can filter hypotheses but cannot replace experiments. The authors expect fields that can check results by computer, such as mathematics, to speed up first.

The main proposal is a four-stage "Hypothesis Exchange Pipeline". An idea is first registered by hashing the prompt, context and research plan that produced it, which the paper calls "Proof of Ideation". AI critics then stake computing credits in a prediction market on whether the idea will hold up. The idea is licensed to a laboratory through tokens the paper calls "Epistemic Options". If the experiment succeeds, a smart contract pays the originator "Parametric Dividends". The same machinery of ledgers, tokens and smart contracts recurs in the other proposals: tiered and paid access to proprietary data, a registry that pays for negative results, bounties for independent replication held in escrow, retroactive funding for ideas that prove useful, public computing reserved for basic research, and a levy on applied licensing to fund it. The authors say a permissioned network run by research institutions and funders could serve in place of a public blockchain. Later sections cover patents for machine-made inventions, liability, international data sharing and the future role of human scientists.

None of this has been built, and the authors identify unsolved problems in most of the proposals. The prediction markets are discussed "Under the assumption that these agentic prediction markets could be made reliable". Separating the agent that proposes an idea from the laboratory that tests it requires a way to verify that the experiment was performed as reported. Paying for negative results invites the mass production of worthless ones, and the stake the authors propose as a deterrent favors well-funded institutions. Retroactive funding requires "an objective method for measuring the impact of a scientific idea over time", and the authors write: "At the moment, we lack this capability."

The paper's premise is that ideas are becoming cheap. It also says of current systems that their hypotheses "often prove unviable under rigorous experimental validation", and that they have been "limited in their ability to deliver profound conceptual leaps". The paper offers no evidence that the proposed markets would allocate experiments better than present arrangements. As an example of progress in mathematics it cites "the AI-derived solution to the Millennium Prize Navier-Stokes problem"; other mathematicians dispute parts of that result ({{navier-stokes-blowup}}).

A Google survey suggests that the shortage of validation already exists: scientists there report a growing backlog of untested hypotheses ({{ai-in-science-early-insights}}). A policy essay by DeepMind staff ({{conjecture-machines}}) argues for funding experimental facilities in response to the same problem.
