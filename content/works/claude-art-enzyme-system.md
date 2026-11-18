---
short: "Enzyme system claim"
title: Claude discovers a novel enzyme system with CRISPR-like repeats
authors:
- Anthropic
org: Anthropic
date: 2026-09-23
type: lab-report
url: https://www.anthropic.com/news/claude-discovers-novel-enzyme-system
links:
- kind: material
  label: 'Yoon et al. for Anthropic: the technical report behind the announcement'
  url: https://www-cdn.anthropic.com/22573675ada52a8ca8a97a1a4b4326b2f208a071.pdf
- kind: response
  label: 'Ilya Finkelstein: a CRISPR and retron researcher''s blog post on the announcement'
  url: https://finkelsteinlab.org/blog/harvesting-and-replenishment-in-biomedicine/
- kind: response
  label: 'CNN: news report on Mario Rodríguez Mestre''s priority claim'
  url: https://www.cnn.com/2026/10/08/science/ai-biology-anthropic-dna-discovery
  date: '2026-10-08'
- kind: response
  label: 'MIT Technology Review: news report on what counts as an AI discovery'
  url: https://www.technologyreview.com/2026/09/28/1145230/when-can-we-say-ai-made-a-scientific-discovery/
  date: '2026-09-28'
license: ''
beat: life-sciences
edition: '003'
drafted_by: Claude Opus 5
well: C8
tier: notice
importance: Notable
novelty: New capability
evidence_type: Agentic search of a metagenomic sequence database, with reanalysis of published RNA sequencing
  and expression of the locus in Escherichia coli
evidence: Contested
independence: Self-reported by developer
read: full
checked:
- Announcement read in full
- Technical report read in full apart from the supplementary figures
- Quotations and figures checked against the announcement, the technical report and the cited news reports
- The sequence data and the laboratory work were not examined
- Neither Mario Rodríguez Mestre nor Anthropic was contacted about the priority claim
- No document settling the sequence of events has been published by either side
coi: Anthropic makes the drafting model, and the work described here is that model's.
found_via: Named by the editor. The monitor's Anthropic feed also carried it.
concerns:
- title: A priority claim over the same observation is unresolved
  body: |
    Anthropic says Claude made the find "with only high-level direction from our scientists" and that "Claude appears to be the first to notice the system's defining features". Days after the announcement, Mario Rodríguez Mestre, who had just completed doctoral work at the University of Copenhagen, said his unpublished research described the same arrays. He told CNN: "It is essentially the same finding. This is not simply a case of two groups studying related protein families or similar biological systems." He also said he had put drafts of his dissertation and related analyses into his private Claude account.

    Mestre does not allege copying. "I am not claiming that Anthropic deliberately took our work. I cannot demonstrate that," he told CNN, and offered two readings: either information about the work reached the model, or "there was considerably more prior scientific knowledge and human direction behind the search than the phrase 'autonomous discovery' suggests". CNN reported that "Anthropic did not respond to an emailed request to comment." MIT Technology Review reported that "Anthropic denies this, but Mestre says he's stopping all use of Claude anyway."

    If the second reading is right, the announcement's claim about how little direction the agents received is weaker. That is the claim about the model's abilities. Neither side has published anything that settles the sequence of events.
  confidence: High that the dispute exists and is unresolved. Whose account is correct cannot be judged
    from the public record.
standfirst: Anthropic's new biology laboratory reports that Claude agents searching a metagenomic database
  noticed an unannotated array of DNA repeats beside a phage reverse transcriptase, which the team names
  ART. What the system does is unknown, the same campaign rerun ten times missed the array every time,
  and a Copenhagen researcher says his unpublished work describes the same arrays.
---

Anthropic has set up a molecular biology laboratory and a research group to look for uncharacterized protein families in sequence databases. Its first published result comes from a campaign in which Claude Code agents, coordinated by a harness of workers, supervisors, curators and editors, surveyed reverse transcriptases across 1.94 billion metagenomic protein clusters. The brief asked for new reverse transcriptase systems identified by new partner-gene associations. The agents built their own sequence profiles, recovered 198,290 reverse transcriptase clusters, sorted them into nine classes, scored 3,564 recurring neighbor families across 10,983 loci, and investigated seventeen candidate partner families in depth. The campaign ran 119 tasks over 949 agent sessions, 215.6 million tokens and 21.5 hours of wall-clock time. Three of the seventeen candidates were confirmed as previously unreported associations. The other fourteen were annotation artifacts, parts of systems already described, or neighbors of the reverse transcriptase.

The result Anthropic announced was not one of those candidates. A worker agent, having rejected the association it was given, asked to look at the non-coding DNA upstream of a group of jumbo-phage reverse transcriptases, read 2,900 nucleotides of one flank directly into its context, and reported a repeating pattern: "The L0050 (228,907 bp logan contig) flank is spectacular: I can see by eye a tandem repeat array". A repeat-counting script it wrote found fourteen copies of a 16-nucleotide repeat separated by unique spacers. Follow-up searches in interactive sessions found 95 reverse transcriptase clusters in this lineage, 28 with a detectable array; arrays hold three to 21 copies of a repeat 15 to 49 nucleotides long, with spacers of 120 to 220 nucleotides and no nearby *cas* genes. The team named the lineage array-associated reverse transcriptases, or ART.

Reanalysis of a published infection time course of *Staphylococcus* phage SA1 shows the array transcribed at every stage, accounting for up to 8% of phage RNA at 15 minutes after infection and resolving into shorter species. Expressing the SA1 locus on plasmids in *Escherichia coli*, from its native sequence and from a heterologous promoter, produced similar discrete short RNAs. The technical report states: "Beyond these observations, we have not shown that the RT is active or that the unit RNAs are its substrates." It adds: "Whether the RT and its partner interact, and what the system does for the phage, are currently unknown."

The report also describes a replication test that the announcement does not mention. The campaign was launched ten more times with the same harness and brief, producing 3,084 task records and 5,632 session transcripts, and "the array was missed in every rerun". The authors write: "We attribute these results to the broad protein search space of RTs and the non-deterministic behavior of the harness." On fixed inputs, where models were handed ART sequences and asked to characterize them, the four most capable Claude models described the array in at least 90% of attempts when the loci were in context, and in as few as 32% of attempts when the sequences had to be fetched with tools.

The announcement and the report differ in some counts. The announcement says the agents "narrowed those to the 20 most compelling candidates"; the report describes seventeen candidate families and nineteen reports. The announcement gives roughly 950 agents, 210 million tokens and 21 hours against the report's 949 sessions, 215.6 million tokens and 21.5 hours.

Responses have divided over what the observation shows. Feng Zhang of MIT and the Broad Institute, quoted in the announcement, said "The identification of RNA-repeat arrays associated with reverse transcriptases is genuinely intriguing and merits further investigation." Ilya Finkelstein, who works on CRISPR and retrons at the University of Texas at Austin, wrote that he would pursue the observation if a student brought it to him, adding "But boy-oh-boy, is the hype getting ahead of the actual science." He also wrote: "Four of six authors are senior molecular biologists and domain experts." Lucas Harrington, quoted by MIT Technology Review, wrote that "finding a weird cluster of genes and repeats is often the easy part. The hard part, and where the real discoveries come from, is figuring out what the system actually does."
