import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)
skipped = sum(1 for l in lines if l.strip()) - len(records)

print(len(records))
print(skipped)
if records:
    print(f"{average_by_city(records)[warmest_city(records)]:.1f}")