# Ontario Auto Product Intelligence

**Independent analytics portfolio case study — synthetic data only. Not affiliated with Allstate Canada.**

A reproducible provincial auto-insurance analytics exercise covering Ontario regions, pricing performance, loss ratios, claims frequency, severity, data quality and decision support.

## Core question

How might a provincial product team identify worsening performance, distinguish frequency from severity effects, and prioritize investigation?

## Quick start

Requires Python 3.10+; no third-party libraries.

```bash
python scripts/generate.py
python scripts/analyze.py
```

This generates `data/synthetic_ontario_auto_quarterly.csv` (720 rows) and `data/regional_year_summary.csv`. Outputs are intentionally generated locally rather than committed so reviewers can reproduce them. The scripts use random seed 42.

## Files

- `scripts/generate.py` — deterministic synthetic portfolio generation
- `scripts/analyze.py` — basic validation and region/year aggregation
- `sql/quality_checks.sql` — SQLite-compatible QA checks after loading CSV as `auto_performance`
- `powerbi/MEASURES.md` — initial DAX definitions and report plan
- `docs/decision_brief.md` — hypothesis, analytical approach, and limitations

## Analytical definitions

- Loss ratio = incurred losses / earned premium
- Claim frequency = claim count / earned exposures
- Claim severity = incurred losses / claim count
- Pure premium = incurred losses / earned exposures

Each row represents a quarter × region × driver segment × coverage. Earned exposures are coverage-level units, **not counts of distinct insured cars across coverages**. Ratios must be calculated from sums, not averaged from individual rows.

The generator intentionally increases modeled claims frequency for some GTA collision and accident-benefits observations in 2026. This is a scenario assumption, **not a finding about Ontario's actual market**.

## Status

**Analytics foundation / work in progress.** The Power BI report and `.pbix` have not yet been created or validated. Next: create three report pages (executive overview, loss drivers, data quality), verify DAX against Python aggregates, publish screenshots and an executive decision brief based on computed results.

## Integrity

No real customer, insurer, or Allstate data is used. This independent case study is not calibrated to regulatory industry benchmarks and cannot justify a real pricing recommendation.
