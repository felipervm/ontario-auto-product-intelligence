import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'data' / 'synthetic_ontario_auto_quarterly.csv'
with source.open(encoding='utf-8', newline='') as file:
    rows = list(csv.DictReader(file))

assert len(rows) == 720, f'Expected 720 rows, got {len(rows)}'
assert len({
    (row['period'], row['region'], row['segment'], row['coverage'])
    for row in rows
}) == len(rows), 'Duplicate observation keys'
assert all(
    float(row['earned_exposures']) > 0
    and float(row['earned_premium_cad']) > 0
    and int(row['claim_count']) >= 0
    and float(row['incurred_losses_cad']) >= 0
    for row in rows
), 'Invalid measure values'

aggregates = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])
measures = ('earned_premium_cad', 'incurred_losses_cad', 'earned_exposures', 'claim_count')
for row in rows:
    key = (row['year'], row['region'])
    for index, name in enumerate(measures):
        aggregates[key][index] += float(row[name])

output = ROOT / 'data' / 'regional_year_summary.csv'
with output.open('w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'year', 'region', 'earned_premium_cad', 'incurred_losses_cad',
        'earned_exposures', 'claim_count', 'loss_ratio', 'claim_frequency',
        'claim_severity_cad'
    ])
    for (year, region), (premium, losses, exposure, claims) in sorted(aggregates.items()):
        writer.writerow([
            year, region, round(premium, 2), round(losses, 2),
            round(exposure, 2), int(claims),
            round(losses / premium, 5), round(claims / exposure, 5),
            round(losses / claims, 2) if claims else 0
        ])
print(f'Validated {len(rows)} records, wrote {output}')
