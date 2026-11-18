---
short: LLM ideas, old directions
title: Large Language Models Extend Known Research But Do Not Create New Research Directions
authors:
- Zhihua Liu
- Kurt Butler
- Damian Machlanski
- Danilo Bueno
- Sotirios A. Tsaftaris
org: University of Edinburgh
date: 2026-10-12
type: paper
url: https://arxiv.org/abs/2610.17439
links:
- kind: material
  label: The research group's code repositories
  url: https://github.com/CHAI-UK
- kind: context
  label: 'Tang and Yang: the distance measures the paper adopts'
  url: https://arxiv.org/abs/2605.27905
license: CC BY-NC-ND 4.0
beat: autonomous-discovery
edition: '004'
well: A2
tier: notice
importance: Notable
novelty: New evidence
evidence: Suggestive
evidence_type: Comparison in an embedding space of 524,308 model-written hypotheses with published papers from 1,325
  research topics
independence: Independent
checked:
- Paper read in full
- Quotations checked against the source
found_via: arXiv monitor.
standfirst: Hypotheses written by eight language models lie as far from the published literature as real papers
  do, or farther. On a new measure of whether an idea points outside the directions a topic already covers, they
  score below real papers in every field and for every model tested. The measure is a proxy computed from embeddings
  of titles and abstracts.
coi: None found. The authors declare no competing interests. No Anthropic model was tested.
read: full
---

Studies in which reviewers rate research ideas have found those from language models to be as novel as researchers' ideas, or more so. This preprint from the University of Edinburgh separates two properties that such ratings combine: how far an idea lies from existing work, and whether it points in a direction that existing work does not already cover.

The authors embedded the titles and abstracts of 26.9 million papers from 1,325 topics in six natural-science fields, using a pretrained embedding model for scientific papers. For each topic a language model received 20 papers and wrote about 50 hypotheses, each as a title and abstract. Eight models from the Gemini, GPT, Qwen and DeepSeek families produced 524,308 in all. Each hypothesis was compared with about 1,000 real papers from the same topic that the model had not been shown. Two measures record distance, to the nearest published paper and to the center of the topic. The third, which the authors introduce and call the orthogonal novelty score, is the share of a paper's embedding that lies outside the subspace spanned by the topic's published literature.

On distance the model-written hypotheses matched real papers or exceeded them: most models placed them farther from the nearest published paper than real papers sit from theirs. On the new score they fell short in every field and for every model. The median hypothesis scored 15% to 23% below the median real paper, and a real paper drawn at random from a topic outscored a hypothesis from the same topic 72% to 82% of the time. Larger models scored lower than smaller ones in the Gemini family, about the same for GPT and Qwen, and higher only for DeepSeek. Giving a model anywhere from 5 to 100 papers made no difference. Choosing the papers farthest from a topic's center, adding five rounds of critique from a second model, and instructing either model to seek unconventional ideas all moved hypotheses farther from published work, and none brought the score level with real papers. The authors conclude that "current LLMs function as engines of normal science" and that presenting them as autonomous discovery agents "risks misallocating our resources".

The conclusion depends on a score that the authors qualify: "A high or low ONS paper is not necessarily novel or unoriginal, respectively." The paper reports no test of the score against papers that scientists regard as having opened new directions. Generation was a single request for a title and abstract, with no tools, data or experiments, and the experiments on context and critique used two small models, Gemini-3.1-Flash-Lite and GPT-5.4-nano. The authors grant that "real AI workflows may diverge from our setup in ways that we did not anticipate". In two places the text describes a difference as not significant and prints a P value below 0.05 beside it.
