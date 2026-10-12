# Power BI setup and initial DAX

First generate `data/synthetic_ontario_auto_quarterly.csv` by running `python scripts/generate.py`. Import it in Power BI Desktop and name the table `AutoPerformance`.

Set year, quarter and claim_count as whole numbers, and monetary and exposure columns as decimal numbers.

```dax
Earned Premium = SUM(AutoPerformance[earned_premium_cad])
Incurred Losses = SUM(AutoPerformance[incurred_losses_cad])
Earned Exposures = SUM(AutoPerformance[earned_exposures])
Claim Count = SUM(AutoPerformance[claim_count])
Loss Ratio = DIVIDE([Incurred Losses], [Earned Premium])
Claim Frequency = DIVIDE([Claim Count], [Earned Exposures])
Claim Severity = DIVIDE([Incurred Losses], [Claim Count])
Pure Premium = DIVIDE([Incurred Losses], [Earned Exposures])
```

Calculate ratios as **SUM(numerator) / SUM(denominator)** rather than averages of row-level ratios.

Proposed report pages:
1. Executive overview: earned premium, incurred losses, loss ratio, quarterly trend, region breakdown.
2. Drivers: frequency and severity by coverage, region and driver segment.
3. Data quality: row count, duplicates, missing data, invalid measure checks.

**Status:** These are measure specifications, not evidence that a Power BI report or `.pbix` file already exists.
