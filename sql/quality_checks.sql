-- SQLite-compatible once CSV is loaded as auto_performance.
SELECT period, region, segment, coverage, COUNT(*) AS duplicate_count
FROM auto_performance
GROUP BY period, region, segment, coverage
HAVING COUNT(*) > 1;

SELECT *
FROM auto_performance
WHERE earned_exposures <= 0 OR earned_premium_cad <= 0
   OR claim_count < 0 OR incurred_losses_cad < 0
   OR period IS NULL OR region IS NULL OR segment IS NULL OR coverage IS NULL;

SELECT year, region,
       ROUND(SUM(incurred_losses_cad) / NULLIF(SUM(earned_premium_cad), 0), 4) AS loss_ratio,
       ROUND(SUM(claim_count) / NULLIF(SUM(earned_exposures), 0), 4) AS claim_frequency
FROM auto_performance
GROUP BY year, region
ORDER BY year, loss_ratio DESC;
