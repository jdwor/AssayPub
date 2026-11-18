---
short: ICML tests LLMs in review
title: 'Use and Effects of LLMs in Peer Review: A Randomized Experiment and Survey at ICML 2026'
authors:
- Sunnie S. Y. Kim
- Wesley Hanwen Deng
- Jennifer Wortman Vaughan
- Buxin Su
- Weijie Su
- Alekh Agarwal
- Sharon Li
- Martin Jaggi
- Daniel G. Goldstein
- Nihar B. Shah
- Miroslav Dudík
author_count: 11
org: Microsoft Research, the University of Pennsylvania, Google Research, Carnegie Mellon University and others,
  with the ICML 2026 organizers
date: 2026-09-16
type: paper
url: https://arxiv.org/abs/2609.19420
license: CC BY 4.0
beat: science-of-science
edition: '003'
well: F6
tier: notice
importance: Major
novelty: New evidence
evidence: Solid
evidence_type: Randomized experiment within a conference review process, with a survey and an AI-text detector analysis
independence: Independent
checked:
- Main text read in full; appendices not read
- Quotations checked against the source
found_via: Returned by the arXiv monitor (science-of-science lens) and by research agent search.
standfirst: ICML 2026 randomly assigned papers to a policy that banned language models in reviewing or one that
  allowed limited use. Acceptance rates were the same under both, and 22.5% of surveyed reviewers under the ban
  reported using a model.
read: full
---

ICML 2026 received 24,661 submissions and used 17,886 reviewers. Authors chose whether their paper could be reviewed under a permissive policy, which let reviewers use language models to understand the paper and polish their own text but not to evaluate the paper or draft the review, or had to be reviewed under a conservative policy that prohibited any use. Authors of 16,877 main-track papers allowed the permissive policy, and the organizers randomly moved 10% of those, 1,686 papers, to the conservative one. A second randomization assigned reviewers who accepted either policy to one of the two.

Outcomes under the two policies barely differed: "73.0% and 73.5% of papers were rejected or withdrawn" and "24.4% and 24.4% were accepted as regular papers". Mean scores were 3.31 and 3.32. Reviews under the permissive policy were about 7% longer and were rated slightly higher by area chairs, a difference that the extra length partly explains.

In an anonymous survey, "22.5% (165 of 732) of the conservative-policy reviewers reported using an LLM despite the prohibition, and 36.5% (155 of 425) of the permissive-policy reviewers reported at least one explicitly disallowed use". An AI-text detector classified 52.2% of sampled reviews under the conservative policy as human-written, and 37.0% under the permissive policy. The authors take that gap as evidence that the assignment did change reviewers' behavior.

The authors write that the results "capture the effects of assigning reviewers to different LLM-use policies rather than specific forms of LLM use, as reviewers did not fully comply". The experiment does not measure how language-model use affects the accuracy of reviews, since quality was measured by area chairs' ratings. The survey had 1,486 respondents from a committee of about 20,000. Highly rated reviewers were overrepresented among them, and reviewers caught violating the policy were excluded.
