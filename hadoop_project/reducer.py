#!/usr/bin/env python3
import sys

# Array to store top 10 salaries
top_salaries = []

# Read input line by line from stdin(mapper output)
for line in sys.stdin:
    # Remove trailing whitespace
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    # Split by tab to get id and company compensation
    parts = line.split('\t')
    if len(parts) != 2:
        continue

    # Extract id and company compensation
    id_field = parts[0]
    company_compensation = parts[1].split(',')

    # Split company compensatoin by comma
    if len(company_compensation) != 2:
        continue

    company = company_compensation[0]
    compensation = company_compensation[1]

    # Add to top_salaries
    top_salaries.append((compensation, id_field, company))

    # Sort and keep only top 10
    top_salaries.sort(reverse=True)
    if len(top_salaries) > 10:
        top_salaries = top_salaries[:10]

# Print results
print("id\tSalary\tcompany")
for compensation, id_field, company in top_salaries:
    print(f"{id_field}\t{compensation}\t{company}")
