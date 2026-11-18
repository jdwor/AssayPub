---
short: Phantom references audited
title: 'Phantom References: Hallucinated Citations That Survive Peer Review at Top-Tier Conferences'
authors:
- Mark Russinovich
- Ram Shankar Siva Kumar
- Ahmed Salem
org: Microsoft
date: 2026-07-01
type: paper
url: https://arxiv.org/abs/2607.00738
links:
- kind: material
  label: RefChecker, the open-source verification pipeline
  url: https://github.com/markrussinovich/refchecker
license: CC BY-NC-ND 4.0
beat: science-of-science
edition: '001'
well: F1
tier: notice
importance: Notable
novelty: Audit or replication
evidence: Suggestive
evidence_type: Automated audit of the bibliographies of accepted papers at four conferences, with a sample of flags
  checked by hand
independence: Independent
checked:
- Abstract, introduction, related work, definitions, method, main findings, discussion of false positives and limitations
  read
- Quotations checked against the source
found_via: Research agent search.
standfirst: An automated audit of accepted papers at ICLR, ICML, NeurIPS and USENIX Security flags under 1% of references
  as likely hallucinated, which still leaves about one paper in twenty at two of the venues with two or more flags.
  The authors report that most of the flags they checked by hand were false alarms, so the counts are upper estimates.
coi: The authors built the tool used for the audit. Its web-search stage ran on Claude Haiku 4.5, made by Anthropic,
  which also makes the model that drafted this assessment.
concerns:
- title: The prevalence figures count automated flags, and most hand-checked flags were false positives
  body: |
    The abstract reports that "roughly one in twenty NeurIPS and USENIX Security papers contains at least two likely hallucinated academic-paper-like references under our strict definition". The limitations section says: "False positives are the primary limitation. Many candidate hallucinations are not hallucinations at all. Of the flags we examined by hand, the majority were set aside as recoverable references". The paper gives no figure for how many flags were examined or what share survived, so the published percentages cannot be converted into a count of fabricated references.

    The authors rely on papers with five or more flags, reasoning that "the five-or-more papers are the cases we can most safely call genuine". That inference is reasonable for fabricated entries and weaker where one extraction fault damages a whole bibliography.
  confidence: High that the headline figures are flags with unmeasured precision, since the paper says so. The size
    of the overstatement cannot be estimated from the paper.
read: partial
read_gap: Parts of the method, the per-venue and per-area results, the adjudicated examples and the conclusion were
  skimmed or not read.
---

A fabricated citation can be detected automatically, because a reference either points to a real work by the named authors or it does not. Three Microsoft researchers built a pipeline, RefChecker, that parses the bibliography of a PDF, looks up each entry in six bibliographic databases, and sends entries that cannot be matched to a language model with web search for a second attempt. They ran it on the accepted, camera-ready papers of ICLR, ICML, NeurIPS and USENIX Security. Only two kinds of failure count: a cited work that cannot be found anywhere, and a real title attached to a substantially different list of authors. Changes of venue, year or publication status do not count.

At the level of single references the rate is low. For 2025 it is between 0.38% and 0.81% of all references, depending on the venue. Proceedings are large, so the same rates mean that 18.7% of ICLR 2025 papers and 26.2% of NeurIPS 2025 papers carry at least one flagged reference. With the threshold raised to two flags and the count limited to references that look like academic papers, the abstract's figure is that "roughly one in twenty NeurIPS and USENIX Security papers contains at least two likely hallucinated academic-paper-like references under our strict definition". The authors report a rise after ChatGPT's release at several venues, most visible among papers with five or more flags, and write that "we do not treat the timing alone as proof that LLM-assisted writing caused the increase". Scanning one venue's 3,703 papers cost about $157.

The authors treat a flag as weak evidence: "The single most consistent lesson from our audit is that an automated flag is a starting point, not a verdict." Of papers with one or two flags they write: "we suspect many are not LLM hallucinations at all, but accidental typos or false positives from our own pipeline". Extraction from PDFs mangles author strings and titles, and works not yet indexed look the same as works that do not exist: "authors we contacted noted that some of their flagged references were for papers not yet published". A stronger model in the search stage reduced false positives substantially at higher cost and was not the one used for the reported numbers.

No paper, author or institution is named: "We do not disclose the identity of any specific paper, author, or institution, and all results are presented in aggregate." That protects authors from an accusation the tool cannot support, and it also means the flagged cases cannot be checked by others. The authors propose that a venue run such a check at submission and hand reviewers a short list of references to confirm.
