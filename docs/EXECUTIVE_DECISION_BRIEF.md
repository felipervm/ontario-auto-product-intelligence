# Executive Decision Brief

**Ontario Auto Product Intelligence**  
*Independent analytical case study · Synthetic data, not Allstate data*

## Decision question

Where is the fictional Ontario auto-insurance portfolio losing performance, and which claim and premium drivers should a provincial product team investigate first?

## Findings

**1. Deteriorating portfolio loss ratio.** In the illustrative dataset, earned premium increases from CAD $64.54M in 2024 to CAD $74.39M in 2026, while incurred losses increase from CAD $35.82M to CAD $46.47M. Loss ratio grows from **55.5% to 62.5%**, or approximately **7.0 percentage points**.

**2. Regional and coverage differences matter.** The Executive Overview shows divergent loss ratios across Ontario regions and product coverages. Higher ratios identify areas for investigation, not necessarily the areas with the greatest absolute financial impact.

**3. Decompose the change before acting.** The Loss Drivers page distinguishes changes in claim frequency, claim severity, and premium per earned exposure. It supports an initial triage of the most material region × coverage × segment combinations.

## Recommended next investigations

1. Calculate **incremental incurred-loss impact** by region, coverage, and driver segment, controlling for earned exposure and premium mix.
2. Decompose the 2024–2026 shift into **frequency, severity, pure premium, and premium adequacy**. Check whether changing portfolio mix explains part of the movement.
3. Validate **claim maturity, reserve development, seasonality, exposure definitions, and statistical credibility** before proposing product or pricing action.

## Data-quality assurance

- **720 synthetic observations** across 12 quarters (2024–2026)
- Unique grain: period × region × driver segment × coverage
- **0** duplicate grain keys
- **0** invalid numeric rows
- **0** rows with missing values
- Annual totals reconcile to independent aggregation scripts

## Interpretation boundaries

All data are **fictional and generated for this portfolio exercise**. The observed deterioration is a modeled stress scenario, not a claim about the actual Ontario insurance market, Allstate Canada, its customers, or its underwriting results. Earned exposures are coverage-specific units, not counts of unique insured vehicles across coverages. Heatmap colors (55%/70% thresholds) are illustrative conventions, not regulatory thresholds.

**Author:** Felipe Mattos
