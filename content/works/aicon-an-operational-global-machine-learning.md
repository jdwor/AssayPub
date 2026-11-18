---
short: Germany's operational AI forecast
title: 'AICON: An operational global machine learning weather forecasting model'
authors:
- Tobias Göcke
- Marek Jacob
- Florian Prill
- Michael Denhard
- Felix Fundel
- Jan Keller
- Roland Potthast
- Hendrik Reich
- Britta Seegebrecht
- Sven Ulbrich
- Arianna Valmassoi
- Sabrina Wahl
org: Deutscher Wetterdienst
date: 2026-08-25
type: paper
url: https://arxiv.org/abs/2608.24651
links: []
license: CC BY 4.0
beat: physical-world
edition: '002'
well: E5
tier: notice
importance: Notable
novelty: New capability
evidence: Solid
evidence_type: A year of forecasts from an operational machine-learning model verified against surface stations and
  radiosondes, with the weather service's own physics-based model as reference
independence: Self-reported by developer
checked:
- Abstract, introduction, data, model, operational, verification and summary sections read
- Quotations checked against the source
- No errors found in the parts read
found_via: Research agent search.
standfirst: Germany's national weather service describes the machine-learning forecast model it has run operationally
  since March 2026, trained on its own 13 km reanalysis. Over a year of verification the model beats the service's
  physics-based model on most surface variables in the first days and does worse on surface pressure and geopotential
  height. Its forecasts now feed official weather warnings.
coi: The authors work at the weather service that built and operates the model and compare it with the service's own
  physics-based system.
read: partial
read_gap: The training details (section 4), the rollout study, the spectral and consistency analyses, the forecasters'
  evaluation and the appendices were not read.
---

AICON is a global machine-learning weather model built by Deutscher Wetterdienst, Germany's national weather service. The paper says: "AICON is in full operational use at Deutscher Wetterdienst since 2nd of March 2026." Most learned weather models are trained on the ERA5 reanalysis at about 31 km and 6-hour steps. AICON is trained on ICON-DREAM, a reanalysis made with the service's own ICON model at 13 km and 3-hour steps, and its graph network is laid out on ICON's native triangular grid. At run time "AICON forecasts are initialized with ICON analysis", so the learned model depends on the physics-based system for both its training data and its starting state.

The verification covers a year of forecasts against surface stations and radiosondes, with ICON forecasts at the same resolution as the reference. The authors report: "In terms of the RMSE the performance of AICON relative to ICON is mixed." AICON does better on most surface variables in the first forecast days, more so in summer than in winter, and on upper-air humidity. It does worse on surface pressure beyond about two days and on geopotential height, especially in winter. Precipitation skill is about equal. In a case study of a category 5 typhoon in April 2026, AICON's track was better than ICON's while the storm was weak and worse once it intensified quickly, and the summary lists among the model's limits "a tendency to underestimate extreme intensities in tropical cyclones and the emergence of spurious precipitation patterns near coastlines at long lead times". The summary also says that "spectral analysis confirms a general damping of mesoscale activity relative to the physics-based ICON reference".

Forecasters assessed AICON daily from September 2025 alongside other models before approval. The model and its software were packaged in a container, a first for the service's forecasting chain. Exact reproducibility of runs, standard for physics-based models, proved too costly, and "bit-wise reproducibility was thus dropped for AICON". After approval the forecasts were released as open data, and "its forecasts became part of the basis for DWD’s weather warnings". The authors write that "DWD was among the first NMSs to make an ML-based forecast system fully operational."

A paper published the same month reports operational use of learned forecasts for tropical cyclones ({{operational-cyclone-forecasting}}).
