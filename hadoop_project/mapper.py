#!/usr/bin/env python3
import sys


# Read input line by line from stdin
for line in sys.stdin:
    # Remove leading/trailing whitespace and split by comma
    line = line.strip()

    # Skip emtpy lines
    if not line:
        continue

    # Split the CSV line by comma
    fields = line.split(',')

    # Skip header or lines that don't have enough fields
    if len(fields) < 3 or fields[0] == 'id':
        continue

    # Extract required fields
    id_field = fields[0]
    company = fields[1]
    compensation = fields[3]

    print(f"{id_field}\t{company},{compensation}")
