---
short: Cyclone forecasts
title: Operational tropical cyclone forecasting with AI
authors:
- Ferran Alet
- Tom R. Andersson
- Ilan Price
- Stratis Markou
- Andrew El-Kadi
- Dominic Masters
- Amy Li
- Samier Merchant
- Natalie Williams
- Gregory Thornton
author_count: 32
org: Google DeepMind and Google Research, with the US National Hurricane Center, Colorado State University, the
  UK Met Office and the University of Waterloo
date: 2026-08-06
type: paper
url: https://www.nature.com/articles/s41586-026-10953-2
links:
- kind: material
  label: Code and weights
  url: https://github.com/google-deepmind/weathernext
- kind: response
  label: 'Chalumeau and others (INRIA and AXA): an independent evaluation of AI cyclone models'
  url: https://arxiv.org/abs/2610.22077
  date: '2026-10-15'
license: CC BY 4.0
beat: physical-world
edition: '002'
well: E2
tier: lead
importance: Major
novelty: New capability
evidence: Solid
evidence_type: Forecast verification against observed storms from 2023 to 2025; real-time operational use
independence: Peer-reviewed
checked:
- Article and methods read in full; supplementary information not read
- Independent evaluation (arXiv 2610.22077) read in full except its appendices
- Quotations checked against the source
- License and publication date confirmed on the journal page
coi: Of the 32 authors, 22 are Google employees who hold Alphabet stock, and five of them have filed a patent on
  the underlying weather model. The work was done under a research agreement between NOAA and Google.
found_via: Research agent search. The monitor's Nature feed covered machine learning only and missed it.
standfirst: Google DeepMind's WeatherNext Cyclones model had a five-day track error of 230 km on storms from 2023
  and 2024, against 370 km for the European Centre's ensemble. The US National Hurricane Center received its forecasts
  during the 2025 season, and the weights are public.
claims:
- claim: At five days ahead, the model's average track error is 230 km, against 370 km for the European ensemble
    (ENS) and 335 km for DeepMind's earlier GenCast.
  status: supported
  note: Evaluated on storms from 2023 and 2024 against the best-track record. The weights are public, so the test
    can be repeated. A preprint from INRIA and AXA, using a different measure, also found better track forecasts
    than ENS on 2025 storms.
- claim: At that accuracy the model gives just over 30 hours more warning than ENS.
  status: supported
  note: From the same evaluation. ENS reaches a 230 km error at about 3.75 days.
- claim: Three-day intensity forecasts are 3.75 knots more accurate than NOAA's regional hurricane model, HAFS.
  status: supported
  note: Compared in the North Atlantic and East Pacific, where HAFS runs. The difference is statistically significant
    from 0.5 to 3.25 days ahead. The model alone is less accurate than the forecasters' intensity consensus at long
    lead times.
- claim: In a simulation, adding the model to the Hurricane Center's track consensus reduces error by 28% on average.
  status: supported
  note: The weights were fitted on 2022 storms and give the model 75% of the weight for latitude and 89% for longitude.
    This was not an operational trial.
- claim: Forecasters at the National Hurricane Center have begun incorporating its guidance into official forecasts.
  status: supported
  note: Four of the authors work at the National Hurricane Center, and the work was done under a research agreement
    between NOAA and Google.
read: full
---

WeatherNext Cyclones is a probabilistic weather model trained on four decades of global atmospheric analyses and on the best-track record of nearly 5,000 tropical cyclones. Starting from the European Centre's operational analysis, it produces ensemble forecasts of a storm's track, intensity and wind radii out to 15 days. The paper is published in *Nature* under a CC BY license. Its 32 authors come from Google DeepMind and Google Research, the US National Hurricane Center, Colorado State University, the UK Met Office and the University of Waterloo.

The authors fixed the design using 2022 as a validation year. They then tested on storms worldwide in 2023 and 2024 and, for 2025, on the North Atlantic and East Pacific, retraining for each test year on data up to the end of the year before. Forecasts were shifted by six hours to match when they would have reached a forecaster, and were scored against the best-track record.

"At the 5-day forecast horizon, the ensemble mean track from WN-C has an average error of 230 km, a 140-km improvement over the 370-km error of ENS", the ensemble of the European Centre for Medium-Range Weather Forecasts. The European ensemble reaches the same error at about 3.75 days, so the new model gives "just over 30 h more advanced warning" at that accuracy. For intensity, the three-day forecast is 3.75 knots more accurate than HAFS, NOAA's regional hurricane model, and the difference is statistically significant from half a day to 3.25 days ahead.

A version of the model has run in real time since June 2025. The paper states that during the 2025 Atlantic season "experimental forecasts from WN-C were provided to the NHC, and forecasters there have already begun incorporating its guidance into their official forecast process". Four of the authors work at the Hurricane Center.

On its own the model is less accurate than the Hurricane Center's intensity consensus at long lead times, and they write that "conventional NWP models still provide substantial value when modelling tropical cyclone intensity". The 28% average improvement from adding the model to the track consensus comes from a simulation with weights fitted on 2022 storms. The model depends on an analysis of the current atmosphere that a physics-based system produces, and it does not forecast rainfall or storm surge.

The evaluation was led by the model's developers. The code and trained weights are public, so others can repeat it.

A preprint posted in October by researchers at INRIA and AXA is a partial independent test. It scored archived forecasts from Google's WeatherNext 2, which uses the same architecture, against the European ensemble on 2025 storms. The Google model put more probability on the observed storm position for about 90% of 41 storms. Peak winds in its gridded fields were too weak, and its ensembles showed calibration errors. The preprint tracked storms in the gridded wind and pressure fields and did not test the separate track and intensity outputs that the *Nature* paper evaluates.
