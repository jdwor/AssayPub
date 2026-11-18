---
short: LLM writing in biomedicine
title: Most biomedical publications show signs of LLM-assisted writing
authors:
- Lena Holzwarth
- Rita González-Márquez
- Dmitry Kobak
org: University of Tübingen; Ghent University
date: 2026-08-11
type: paper
url: https://arxiv.org/abs/2608.10715
links: []
license: CC BY-SA 4.0
beat: science-of-science
edition: '002'
well: F3
tier: notice
importance: Notable
novelty: New evidence
evidence: Suggestive
evidence_type: Word-frequency analysis of 1,194,287 open-access full texts from PubMed Central, 2017 to 2025, with
  the estimator validated on simulated data
independence: Independent
checked:
- Main text read in full, and the methods through the construction of the dataset
- Quotations checked against the source
- No errors found
found_via: Research agent search.
standfirst: A new estimator applied to 1.2 million open-access biomedical papers puts the share showing signs of language-model
  assistance at 77% for 2025 and 89% for December 2025. The figure counts any use anywhere in a paper, editing included,
  and rests on extrapolating pre-2023 word frequencies three years forward.
coi: None found.
read: full
---

Earlier studies counted the excess use of a few hundred style words, such as *these*, *potential* and *delves*, in abstracts written after 2022, and put the share of papers written with help from a language model at 12% to 16% for 2024. The authors, who wrote one of those studies, argue here that "frequency gaps systematically underestimate the true fraction of LLM-assisted articles". They propose an estimator meant to recover the share itself and apply it to the full text of 1,194,287 open-access biomedical papers from PubMed Central, published from 2017 to 2025.

For a set of marker words, the method tracks the share of documents that contain at least one of them. A line fitted to 2018–2022 gives the share expected without language models. The gap between observed and expected, rescaled, is a lower bound on the share of documents written or edited with a model. The authors pick the set of words that makes the bound largest, subject to a cap on its standard error, and then "assume that our lower bound is acceptably tight and use it as the estimate of LLM usage frequency". In a simulation with known answers the estimate came within 0.02 of the truth.

For whole papers the estimates are 19% in 2023, 52% in 2024, 77% for 2025 and 89% for December 2025. The authors note that "our approach detects LLM usage in any part of the paper", so longer texts score higher. On random passages of 255 words the figures for December 2025 are 68% for discussion sections and 32% for methods sections. By country of the first author, the 2025 estimates run from 85% for South Korea and 82% for China to 28% for the United Kingdom. Countries where most people speak English natively come to 37% together and the rest of the world to 72%. The marker words were much rarer in the second group before 2023, and by 2025 their frequencies had nearly met, "indicating strong linguistic convergence driven by the LLM usage".

The headline figure counts a paper if a model touched any part of its text, whether to draft, translate or copy-edit. It does not measure how much of the text a model wrote or how good the paper is. It also rests on carrying a 2018–2022 trend three years forward, which the authors say "becomes more tenuous as we move away from this date". Writers who pick up the models' vocabulary without using them would inflate the estimate, and writers who avoid the marker words would lower it. The simulation tests the estimator under its own assumptions. As outside support the authors cite surveys in which over 70% of researchers report using models for writing, and add: "People are likely using LLMs more often than they are admitting when surveyed."

A study of astronomy papers the following month reached a similar conclusion with a different statistical model ({{more-than-half-of-recent-astronomy}}).
