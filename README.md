# Ontario Auto Product Intelligence

**Independent Power BI case study · Ontario automobile insurance · Synthetic data only**

An end-to-end provincial product-performance intelligence exercise demonstrating how a product analyst can monitor premium and claims performance, identify deterioration, investigate loss drivers, and validate the reliability of reporting.

> **Portfolio project, not an Allstate Canada project.** All data and modeled effects are fictional; there is no affiliation with, or access to data from, Allstate Canada or any other insurer.

## Report walkthrough

| Page | What it answers |
| --- | --- |
| **Executive Overview** | Where are premiums, incurred losses, and loss ratio trending? Which regions and coverages warrant investigation? |
| **Loss Drivers** | Is deterioration driven by claim frequency, claim severity, or premium adequacy? How does it differ by segment? |
| **Data Quality** | Are quarterly records complete, nonduplicated, numerically valid, and consistent with the source summary? |

The final Power BI project retains **three pages**, interactive page-navigation controls, year/region/coverage/driver-segment slicers, and DAX measures for quality checks. The screenshots selected for this release show the year 2025 to demonstrate a historical view, while the decision brief compares 2024 to 2026.

### Key illustrative findings

| Metric | 2024 | 2025 | 2026 |
| --- | ---: | ---: | ---: |
| Earned premium | CAD $64.54M | CAD $70.89M | CAD $74.39M |
| Incurred losses | CAD $35.82M | CAD $39.98M | CAD $46.47M |
| Loss ratio | **55.5%** | **56.4%** | **62.5%** |

The modeled loss ratio increases by approximately **7 percentage points** from 2024 to 2026. This is a scenario result, **not** evidence that Ontario insurers' actual performance changed by this amount.

### Quality controls

- 720 rows: **12 quarters × 5 regions × 3 driver segments × 4 coverages**
- No duplicate observation keys
- No missing values or invalid numeric records
- Three Power BI data-quality cards show **0**, and the quality status displays **ALL PASSED**
- Annual premium, loss, and claim totals reconcile to an independently aggregated CSV

## Run the data pipeline

Requires Python 3.10+; no third-party packages.

```powershell
python scripts/generate.py
python scripts/analyze.py
```

The pipeline produces `data/synthetic_ontario_auto_quarterly.csv` and `data/regional_year_summary.csv`. Outputs are ignored by Git; they are reproducible using seed 42.

## Power BI report

The working report was developed in **Power BI Desktop** and is maintained as a **Power BI Project (PBIP)**. The interactive `.pbip` project is a Power BI Desktop artifact, not a hosted web application. To review it locally, open its `.pbip` file in Power BI Desktop and refresh the local synthetic CSV source if prompted.

> Source artifact upload and screenshot assets are tracked separately. A link or preview should only be considered available after those binary files appear in this repository.

## Analytical definitions

- **Loss ratio** = incurred losses / earned premium
- **Claim frequency** = claim count / earned exposures
- **Claim severity** = incurred losses / claim count
- **Pure premium** = incurred losses / earned exposures

All ratios use **ratios of sums**, not averages of row-level ratios. Earned exposures are coverage-level exposure units and must not be interpreted as distinct insured vehicles when summed across coverages.

## Files and documentation

- [Executive decision brief](docs/EXECUTIVE_DECISION_BRIEF.md) — key findings, questions, and limitations
- [Data generator](scripts/generate.py) — reproducible synthetic source
- [Validation and aggregation](scripts/analyze.py) — data checks and regional-year KPI summary
- [SQL QA checks](sql/quality_checks.sql) — optional independent checks
- [Power BI measures reference](powerbi/MEASURES.md) — base metric logic

## Scope and limitations

Synthetic claims effects are intentionally injected into the scenario, especially for 2026 GTA-area collision and accident-benefits cohorts. The dashboard supports investigation, not causal attribution or actual pricing changes. A real pricing recommendation would require mature claims, loss-development review, exposure comparability, actuarial credibility, business constraints, and relevant regulatory requirements.

**Author:** Felipe Mattos · Independent portfolio case study
