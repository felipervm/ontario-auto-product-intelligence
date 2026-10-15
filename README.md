# Ontario Auto Product Intelligence

**From portfolio performance to better decisions.**

*Independent Power BI case study · Ontario auto insurance · Synthetic data*

When an auto insurance portfolio starts underperforming, a higher loss ratio tells you **something changed**—but not **why**, or what to investigate first.

I created a fictional Ontario auto portfolio and a three-page Power BI report to explore how a Provincial Product Analyst could monitor performance, separate possible claims and premium drivers, and check the reliability of the numbers before recommending action.

> **Independent portfolio study, not an Allstate Canada project.** All data, trends, and findings are fictional. No insurer data was accessed, and this work is not affiliated with or endorsed by Allstate Canada.

## See the Power BI report

No Power BI installation is needed to review these previews. Each image shows one page of the report.

### 01 · Executive Overview — Where is performance changing?

Track earned premium, incurred losses, and loss ratio, then compare regions and coverages to identify areas worth investigating.

![Power BI Executive Overview dashboard showing Ontario auto insurance performance](assets/screenshots/executive-overview.png)

### 02 · Loss Drivers — What might explain the change?

Look beyond a single loss ratio. Examine claim frequency, claim severity, premium adequacy, and how patterns differ by region, coverage, and driver segment.

![Power BI Loss Drivers dashboard for a synthetic Ontario auto insurance portfolio](assets/screenshots/loss-drivers.png)

### 03 · Data Quality — Can we trust the numbers?

Before drawing conclusions, verify that the underlying records are complete, unique, numerically valid, and consistent with independent summaries.

![Power BI Data Quality dashboard with validation checks](assets/screenshots/data-quality.png)

## An illustrative finding

In the fictional dataset, earned premium rises between 2024 and 2026—but incurred losses rise faster.

| Portfolio measure | 2024 | 2026 |
| --- | ---: | ---: |
| Earned premium | CAD $64.54M | CAD $74.39M |
| Incurred losses | CAD $35.82M | CAD $46.47M |
| **Loss ratio** | **55.5%** | **62.5%** |

**The decision is not simply “fix the loss ratio.”** A product team would first investigate which regions and coverages contributed to deterioration, how claim frequency and severity changed, whether portfolio mix or premium adequacy played a role, and whether the data is sufficiently reliable.

These are deliberately modeled results—not real Ontario market trends, not Allstate performance, and not evidence supporting an actual pricing change.

[**Read the two-minute executive decision brief →**](docs/EXECUTIVE_DECISION_BRIEF.md)

## What this demonstrates

- **Performance monitoring:** surface KPI trends and areas requiring attention
- **Business analysis:** move from an aggregate change toward possible underlying drivers
- **Decision support:** suggest next investigations instead of overstating causation
- **Reporting integrity:** validate data before communicating conclusions
- **Clear communication:** make the findings accessible to non-technical stakeholders

## How the study was built

I created **720 synthetic quarterly observations** covering 12 quarters, five Ontario regions, three driver segments, and four coverages. Python generates and validates the dataset; the Power BI report contains three pages with filters and analytical measures. Separate SQL checks and a reproducible aggregation provide additional quality assurance.

The synthetic scenario contains **zero missing values, zero duplicate observation keys, and zero invalid numeric records**. Annual premium, losses, and claims reconcile against separately aggregated summaries.

### Explore the supporting work

- [Executive decision brief](docs/EXECUTIVE_DECISION_BRIEF.md) — findings, limitations, and recommended investigations
- [Power BI project](powerbi/OntarioAuto/) — editable Power BI Desktop project
- [Python data generator](scripts/generate.py) and [analysis/validation](scripts/analyze.py)
- [SQL quality checks](sql/quality_checks.sql) and [Power BI measures](powerbi/MEASURES.md)

<details>
<summary><strong>Technical notes & reproducibility</strong></summary>

Requires Python 3.10+ with no third-party Python dependencies for the data pipeline.

```powershell
python scripts/generate.py
python scripts/analyze.py
```

The commands produce `data/synthetic_ontario_auto_quarterly.csv` and `data/regional_year_summary.csv`. Generated outputs are excluded from Git, but can be reproduced with seed 42.

The Power BI report uses a Power BI Project (PBIP), not a hosted web app. To interact with it locally, open `powerbi/OntarioAuto/OntarioAuto.pbip` in Power BI Desktop and refresh the CSV source if requested. The screenshots above are for immediate visual review.

**Analytical definitions**

- Loss ratio = incurred losses / earned premium
- Claim frequency = claim count / earned exposures
- Claim severity = incurred losses / claim count
- Pure premium = incurred losses / earned exposures

Ratios are calculated as ratios of sums rather than averages of row-level ratios. Exposure counts are coverage-specific, not counts of distinct insured vehicles across coverages.

</details>

## Limits of this case study

The dataset intentionally introduces fictional claims deterioration, particularly in 2026 GTA-area collision and accident-benefits cohorts. The dashboard is an **investigation aid**, not proof of a cause or a basis for real pricing or underwriting decisions. Actual actions would require mature claims, loss-development analysis, comparable exposures, actuarial review, business constraints, and applicable regulatory considerations.

---

**Felipe Mattos** · Independent portfolio case study

I am interested in analytics that connects data quality, business performance, and practical decisions.

[LinkedIn](https://www.linkedin.com/in/felipervm) · [GitHub](https://github.com/felipervm)
