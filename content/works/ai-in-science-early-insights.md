---
short: 'Google: how scientists use AI'
title: 'AI in Science: Early Insights'
authors:
- Mihai Codreanu
- Alex Imas
- Juan Mateos-Garcia
- Joseph Emmens
- Evalyne Muiruri
- Arthur Turrell
- Julian Jacobs
- Atoosa Kasirzadeh
- Ana Trisovic
- Yiyuan Chen
- Tanya Rodchenko
- Catherine Pollard
- Scott Strand
- Daniel Rock
- Zanna Iscenko
- Fabien Curto Millet
- Neil Thompson
- James Manyika
org: Google and Google DeepMind, with academic co-authors
date: 2026-09-15
type: paper
url: https://arxiv.org/abs/2609.28504
links:
- kind: material
  label: The paper as a web page
  url: https://arxiv.org/html/2609.28504v2
license: CC BY-NC-ND 4.0
beat: science-of-science
edition: '003'
well: F5
tier: lead
importance: Major
novelty: New evidence
evidence: Suggestive
evidence_type: Usage-log analysis, bibliometrics of a model inventory, and a survey
independence: Self-reported by developer
checked:
- Main text read in full; the appendices on classifier validation and the survey were consulted
- Quotations checked against the source
- License and dates confirmed on arXiv
- No errors found in the main text
coi: Most authors work for Google, whose product supplies the usage data. The survey was fielded for Google DeepMind
  by a third party.
found_via: Named by the editor. Also returned by the arXiv monitor (general and science-of-science lenses).
standfirst: A Google-led study combines Gemini usage logs, an inventory of specialized models and a survey of 637
  scientists. Respondents report saving about seven hours a week with AI and spending a large share of that time
  verifying its output.
abstract: 'Scientific progress is a key driver of economic growth and prosperity. There is great excitement - but
  also concerns - about the impacts of AI on science, but so far little data. We provide early insights on this
  from three data sources: a sample of 15 million Gemini interactions, an inventory of over 2,600 specialized AI
  models across disciplines, and a survey of over 600 scientists. We map these data to a new taxonomy of scientific
  tasks to study how scientists are using AI. Four main findings emerge. First, we find broad adoption and coverage:
  scientists use AI more than most other occupations. Specialized AI models have broad disciplinary coverage and
  are highly cited. Nearly half of the scientists surveyed report using some form of AI every day. Second, we document
  evidence that LLMs (proxied through Gemini usage) and specialized models act as complements-- LLMs are used for
  general analysis, coding, and manuscript preparation, while specialized models provide domain-specific predictions,
  data generation and classification. Third, scientists report large productivity gains from using AI: a saving
  of nearly 7 hours per week, time which is primarily re-invested in more research. Finally, we show that AI is
  already changing the scientific process. As some stages of scientific research become easier, bottlenecks shift
  downstream. Scientists report an increased backlog of untested hypotheses and substantial demand for output verification.
  Our findings suggest that AI holds significant potential to increase scientific productivity. However, as with
  other sectors, its ultimate impact will be governed by complex task interdependencies and investment into the
  elimination of emerging bottlenecks.'
abstract_note: From arXiv's public metadata.
claims:
- claim: Scientists use AI more than most other occupations. Life, physical and social science occupations use Gemini
    at about 2.7 times their share of the US workforce.
  status: self-reported
  note: From Google's usage logs, which are not public. Occupation is inferred by a classifier that was 71.6% accurate
    on synthetic test data.
- claim: General language models and specialized scientific models are used for different tasks.
  status: self-reported
  note: The association between the two kinds of use falls from about 0.6 at the coarsest task level to 0.2 at the
    finest. At the finest level the classifier assigned the right task in about 30% of test cases, and the models'
    tasks are taken from the abstracts of the papers that introduced them.
- claim: Scientists save about 6.9 hours a week.
  status: self-reported
  note: Respondents' estimates from a non-probability sample of 637. Output was not measured.
- claim: About 44% of respondents say their main bottleneck moved downstream toward experiments and verification;
    about 14% say it moved upstream.
  status: self-reported
  note: Survey responses.
- claim: 49% of respondents say AI pushes them toward safer, more incremental questions; 28% say it lets them take
    on riskier ones.
  status: self-reported
  note: Respondents' descriptions of their own choices. The paper does not measure the riskiness of published work.
read: full
---

The paper draws on three sources. The first is a sample of about 15 million anonymized Gemini conversations from early April 2026, of which roughly 360,000 were classified as scientific work. The second is an inventory of 2,690 specialized models, such as protein structure predictors and weather emulators, with their citation records. The third is a survey of 637 scientists in the United States and the United Kingdom, run for Google DeepMind by the research organization More in Common in July and August 2026. Of the respondents, 356 hold senior roles such as principal investigator or R&D manager, and at least 368 work in industry. The authors map all three sources onto a taxonomy of research tasks from MIT FutureTech.

In the logs, people in life, physical and social science occupations account for about 2.7 times as much Gemini use as their share of the US workforce. About 42% of scientific conversations involve analyzing or modeling quantitative data and about 14% involve communicating findings. Computer science and the other physical sciences account for 55.3% of scientific conversations, and the life and health sciences for 23%.

In the inventory, 49% of the papers that introduced a model are in the top 1% of citations for their field. The authors note that the inventory was assembled from sources that select for notable models. They compare the tasks the models perform with the tasks in the Gemini logs. At the coarsest level of the taxonomy both concentrate on quantitative analysis. At the finest level the association between the two falls to 0.2, which the authors read as evidence that the two kinds of tool complement each other. They caution that part of the decline comes from classifier error: at that level the classifier assigned the right task in about 30% of test cases.

In the survey, almost half of respondents use some form of AI every day and nearly three quarters say it saves them time on net. The average reported saving is 6.9 hours a week. About 44% said their main bottleneck had moved downstream, toward experiments and verification, and about 14% said it had moved upstream. About 41% reported a larger backlog of untested hypotheses and about 25% a smaller one. Of those who saved time, 46% spent more than a quarter of the saving checking AI output. Asked about their choice of problems, 49% said AI pushed them toward safer, more incremental questions and 28% said it let them take on riskier ones.

The time savings are respondents' own estimates, and the paper does not measure research output. The authors write that "our results establish associations rather than causality". They describe the survey as "a screened non-probability sample rather than a representative one", report it without margins of error, and say that scientists who already use AI may have been more likely to answer. The usage logs come from Google's consumer products and unpaid API use and exclude enterprise customers, and the authors write that "Generalization should be done with caution".

Anthropic published a comparable study of Claude usage in November ({{how-researchers-use-claude}}). It also finds that data analysis is the largest use, that computer science is overrepresented relative to its number of researchers, and that the health sciences are underrepresented.
