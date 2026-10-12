import csv
import random
from pathlib import Path

random.seed(42)
ROOT = Path(__file__).resolve().parents[1]
regions = {
    'Toronto': (1.22, 1.14), 'GTA Other': (1.08, 1.03),
    'Ottawa': (0.92, 0.93), 'Southwestern Ontario': (0.96, 0.98),
    'Northern Ontario': (1.04, 1.10),
}
segments = {
    'Standard': (1.0, 1.0), 'Preferred': (1.22, 0.77),
    'New Driver': (1.44, 1.42),
}
coverages = {
    'Collision': (1.25, 1.2), 'Comprehensive': (0.65, 0.68),
    'Accident Benefits': (1.05, 1.12),
    'Third Party Liability': (1.1, 0.95),
}
rows = []
for year in (2024, 2025, 2026):
    for quarter in range(1, 5):
        for region, (risk, sev) in regions.items():
            for segment, (price, frequency) in segments.items():
                for coverage, (premium_factor, claim_factor) in coverages.items():
                    exposure = round(random.uniform(150, 520) * (1 + .035 * (year - 2024)), 2)
                    price_per_exposure = round(
                        650 * price * premium_factor * (1 + .045 * (year - 2024)), 2
                    )
                    earned_premium = round(exposure * price_per_exposure, 2)
                    rate = .045 * risk * frequency * claim_factor
                    if year == 2026 and region in ('Toronto', 'GTA Other') and coverage in ('Collision', 'Accident Benefits'):
                        rate *= 1.22
                    claim_count = max(0, round(exposure * rate + random.gauss(0, 2)))
                    severity = round(
                        8500 * sev * (1 + .075 * (year - 2024)) * random.uniform(.88, 1.12), 2
                    )
                    incurred_losses = round(claim_count * severity, 2)
                    rows.append([
                        f'{year}Q{quarter}', year, quarter, region, segment, coverage,
                        exposure, earned_premium, claim_count, incurred_losses
                    ])

path = ROOT / 'data' / 'synthetic_ontario_auto_quarterly.csv'
path.parent.mkdir(parents=True, exist_ok=True)
with path.open('w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'period', 'year', 'quarter', 'region', 'segment', 'coverage',
        'earned_exposures', 'earned_premium_cad', 'claim_count', 'incurred_losses_cad'
    ])
    writer.writerows(rows)
print(f'Generated {len(rows)} synthetic rows: {path}')
