---
short: "Drug development with Claude"
title: Early progress on accelerating drug development with Claude
authors:
- Anthropic
org: Anthropic
date: 2026-10-27
type: lab-report
url: https://www.anthropic.com/research/early-progress-drug-development
links:
- kind: material
  label: 'Anthropic: technical report on the bispecific bridging antibody for LAMA2-related muscular dystrophy'
  url: https://assets.claude.com/52e1f5d50c47ca3818f56704c27cf19e59b62e77.pdf
- kind: response
  label: 'Heidi Ledford, Nature: news report on the purchase of Mithril Medicine and who develops a drug'
  url: https://www.nature.com/articles/d41586-026-03640-9
  date: '2026-11-11'
- kind: response
  label: 'Derek Lowe: commentary on predictions that major diseases will soon be cured'
  url: https://www.science.org/content/blog-post/stop-it-just-stop-it
  date: '2026-11-13'
- kind: response
  label: 'In the Pipeline feed: the text of Lowe''s post'
  url: https://www.science.org/blogs/pipeline/feed
  date: '2026-11-13'
license: ''
beat: chemistry-medicine
edition: '004'
drafted_by: Claude Opus 5
well: D5
tier: lead
importance: Notable
novelty: New evidence
evidence_type: Six partner case studies described by the developer, with one accompanying technical report
  containing a pilot study in mice
evidence: Preliminary
independence: Self-reported by developer
read: full
checked:
- Announcement read in full
- Anthropic's own technical report read in full apart from the supplementary figures
- Figures and quotations checked against those two documents and the Nature news report
- The technical reports from Generate Biomedicines, Divergence Labs, BigHat Biosciences and Enveda were
  not opened; the BigHat page could not be read without JavaScript
- No errors found in the announcement or in Anthropic's technical report
- A Wall Street Journal article of November 8, reported to be critical of the release, could not be opened
  and is not used here
coi: Anthropic makes the drafting model, and the work described here is that model's.
found_via: Named by the editor. The monitor's Anthropic feed also carried it.
standfirst: Anthropic describes work with six drug developers and its own purchase of a one-person biotechnology
  company. The reported results include a 1,010-variant antibody optimization campaign, an 89% cut in
  manufacturing document review, and a bispecific antibody that doubled forelimb strength in a pilot study
  of 7 mice. All of it is preclinical, and the companies supplied the numbers.
claims:
- claim: Working with Divergence Labs, Claude generated roughly 35,000 antibody designs in about a month,
    of which early tests found 3 that bound IgE and 20 that dislodged it from immune cells, 3 of them better
    than the standard medication.
  status: self-reported
  note: The figures come from Anthropic's post. The two arms have not yet been combined into a candidate
    molecule.
- claim: With BigHat Biosciences, about 1,010 variants of two antibody fragments were made and tested in
    about 10 weeks; the best bound more than 10 times more tightly, one stayed in solution at a temperature
    18 °C higher and one clumped more than 100 times more slowly.
  status: self-reported
  note: Anthropic's post gives no baseline campaign, so the gain over BigHat's usual practice cannot be
    judged.
- claim: On 1,061 pages of Enveda manufacturing documents, Claude found all 11 issues human reviewers had
    spotted and 7 they had missed, and cut human review time by 89%, from over 25 hours to under three.
  status: self-reported
  note: Anthropic's post gives the counts without characterizing the seven additional flags; false positives
    are not reported.
- claim: A bispecific bridging antibody from Mithril Medicine roughly doubled nerve-evoked peak force and
    forelimb grip strength in laminin-α2-deficient mice.
  status: self-reported
  note: The technical report gives the data for 7 treated and 4 vehicle-treated mice. Groups were enrolled
    in sequence, litters were not randomized, and the authors report P = 0.057 when litters are the unit
    of analysis.
- claim: A drug candidate from this work could be ready to start human trials as soon as late 2028.
  status: unverified
  note: A forecast. Nothing in either document is in clinical development.
---

Anthropic's life sciences team describes research partnerships with six organizations that develop medicines (BigHat Biosciences, Bristol Myers Squibb, Divergence Labs, Enveda, Generate Biomedicines and The Column Group) and programs of its own. The organizing argument is that the obstacles to faster drug development are spread across the whole process: "There is no single problem to solve; the bottlenecks are distributed all throughout the drug development process." Each case study is paired with a technical report from the partner.

The reported results span that range. At Generate Biomedicines, six scientists used Claude Code to shorten part of the genetic instructions for a CAR T-cell therapy; one design was about 70% shorter than the standard version and let immune cells make roughly ten times as many receptors. At Divergence Labs, which is building a two-armed molecule to strip IgE off immune cells, Claude produced about 35,000 antibody designs in a month, from which three IgE binders and twenty molecules that dislodged IgE emerged. At BigHat Biosciences, Claude was connected to the company's laboratory data system and proposed changes to two antibody fragments; about 1,010 variants were made and tested over ten weeks, and the best bound more than ten times more tightly, with one fragment staying in solution 18 °C higher and another clumping more than a hundred times more slowly. Partway through, Claude and a researcher concluded that the standard stability and aggregation measures were misleading, proposed different ones and a protocol change, and the post says "the main predictions held". At Enveda, where manufacturing chemists had been spending up to 75% of their time on paperwork, Claude reviewed 1,061 pages, matched all eleven issues human reviewers had found and flagged seven more, and cut review time by 89%; it also drafted a regulatory document in four hours that would have taken about three months by hand. With The Column Group, Anthropic is helping set up a company, Pleiades, whose first Claude skill, for judging whether a drug target is worth pursuing, has been evaluated on 45 target-disease pairs. The Bristol Myers Squibb work is newer and concerns clinical trial planning; the post quotes Michael Pourdehnad of BMS saying that "From a single prompt, Claude generated a robust initial analysis that helped inform our assessment of different development options, which would otherwise take days to complete."

Anthropic also bought Mithril Medicine, a company with one full-time employee working on two rare forms of muscular dystrophy, and says its founder used Claude to run contracts, logistics and experiments across eleven external laboratories. The accompanying technical report describes two bispecific antibodies intended to bridge laminin-α4 to β-dystroglycan and so restore the anchorage that laminin-α2-deficient muscle has lost. Both were "tool molecules built on published variable regions", which the post does not say. Both bound their targets at nanomolar affinity and bridged dystroglycan-overexpressing cells to a laminin-α4 fragment in vitro. In a six-week pilot in dyW mice, the report says that "mice treated with the tetravalent construct developed about twice the peak force and grip strength of vehicle-treated mice".

"The main limitations concern the pilot study, in which groups were enrolled in sequence, vehicle followed a different regimen", the authors write, and each litter received one treatment without randomization; "litter means gave P = 0.057, the smallest value possible with seven litters"; and "Because six treated groups (Supplementary Table S6) and at least 11 endpoints were examined, a chance finding is possible." Four to seven treated mice remained per group at week six, so groups may differ by survival as well as by treatment. The tetravalent group was tested 126 and 161 days after the vehicle group, with a move of the colony in between, and wild-type grip strength rose 2.65-fold between the two sessions. Exposure cannot be related to effect, because muscle levels were measured only for the other construct. These qualifications come from the report; the announcement describes the same work as "promising results in mice".

Anthropic says the work is "mostly preclinical" and that it plans to extend into clinical trials as programs advance. Reporting for *Nature*, Heidi Ledford counted the people involved in the Mithril programs: the two antibodies were developed with part-time consultants and "at least five contract research organizations". She quotes Jeb Keiper of Third Rock Ventures saying "It takes a village to develop a drug." Derek Lowe, writing about Dario Amodei's statement that cancer, Alzheimer's and heart disease "will be relics of the past in, I think, less than a decade", replied: "Stop talking about how we're going to cure cancer and everything else in X number of years (or just Real Soon Now in general) and spend more time going out and doing it."

The headline numbers come from companies reporting on their own collaborations, and none of the programs has been tested in a person.
