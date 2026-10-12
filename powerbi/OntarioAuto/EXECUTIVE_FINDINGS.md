# Ontario Auto Product Intelligence — Executive decision brief

**Independent case study | Synthetic data only | Not affiliated with Allstate Canada**

## Executive finding

Across the simulated Ontario auto portfolio, incurred losses grew faster than earned premium. The aggregate loss ratio increased from **55.5% in 2024** to **62.5% in 2026** (approximately **7.0 percentage points**). This indicates deterioration in this fictional scenario; it is not evidence of real market behavior.

## Product-team questions to prioritize

1. **Frequency versus severity:** Is loss-ratio deterioration explained mainly by increasing claims per earned exposure, greater incurred losses per claim, or both?
2. **Segment and region:** Which coverage × region × driver-segment combinations account for the largest dollar contribution to the loss-ratio change, rather than only showing high percentages?
3. **Premium adequacy:** Has earned premium per coverage-level earned exposure kept pace with pure premium, and has the portfolio mix changed?

## Next analytical actions

- Validate exposure comparability and claim definitions before using the observed differences.
- Investigate maturity of claims, reserve development, frequency/severity mix and concentration by segment.
- Prioritize investigation by incremental incurred-loss impact; do **not** infer that a pricing intervention is warranted from this synthetic dashboard alone.

## Data-quality checks

- **720** quarterly rows across 12 periods; expected grain = period × region × segment × coverage.
- **0 duplicate grain keys**, **0 invalid numeric records**, **0 missing values** in the embedded dataset.
- The report measures for these checks now convert empty table results to zero, while retaining the existing report layout.

## Boundaries

Data are fully synthetic and intentionally include modeled stress. Earned exposures are **coverage-level** units, not distinct insured vehicles summed across coverages. The red/amber/green loss-ratio thresholds in the dashboard are illustrative reporting conventions, not regulatory standards. No actual insurance company, customer, or policyholder data were used.
