#!/usr/bin/env python3
"""Roll two dice many times and show how often each total comes up."""

import random
import statistics

ROLLS = 10000

totals = [random.randint(1, 6) + random.randint(1, 6) for _ in range(ROLLS)]

print(f"Rolled two dice {ROLLS:,} times\n")

for total in range(2, 13):
    count = totals.count(total)
    percent = count / ROLLS * 100
    bar = "#" * round(percent)
    print(f"{total:>2} | {bar:<17} {percent:5.2f}%")

print(f"\nMean roll:   {statistics.mean(totals):.2f}  (expected 7.00)")
print(f"Most common: {statistics.mode(totals)}")
