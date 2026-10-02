#!/usr/bin/env python3
"""Simulates a week of orders at a campus coffee cart and prints a summary
with a text bar chart. Uses only the Python standard library."""

import random
import statistics

DRINKS = ["Latte", "Cold Brew", "Cappuccino", "Matcha", "Chai", "Espresso"]
PRICES = {"Latte": 5.25, "Cold Brew": 4.75, "Cappuccino": 4.95,
          "Matcha": 5.50, "Chai": 4.50, "Espresso": 3.25}
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]


def simulate_week(seed=None):
    rng = random.Random(seed)
    week = {}
    for day in DAYS:
        n_orders = rng.randint(40, 120)
        week[day] = [rng.choice(DRINKS) for _ in range(n_orders)]
    return week


def bar(value, max_value, width=30):
    filled = round(width * value / max_value) if max_value else 0
    return "#" * filled


def main():
    week = simulate_week()

    print("=" * 50)
    print("  CAMPUS COFFEE CART - WEEKLY REPORT")
    print("=" * 50)

    daily_counts = {day: len(orders) for day, orders in week.items()}
    busiest = max(daily_counts.values())
    print("\nOrders per day:")
    for day, count in daily_counts.items():
        print(f"  {day}  {bar(count, busiest):<30} {count}")

    totals = {drink: 0 for drink in DRINKS}
    for orders in week.values():
        for drink in orders:
            totals[drink] += 1
    top = max(totals.values())
    print("\nOrders per drink:")
    for drink, count in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"  {drink:<11} {bar(count, top):<30} {count}")

    revenue = sum(PRICES[d] * c for d, c in totals.items())
    counts = list(daily_counts.values())
    print("\nSummary:")
    print(f"  Total orders:      {sum(counts)}")
    print(f"  Mean orders/day:   {statistics.mean(counts):.1f}")
    print(f"  Std dev orders/day:{statistics.stdev(counts):>6.1f}")
    print(f"  Best seller:       {max(totals, key=totals.get)}")
    print(f"  Total revenue:     ${revenue:,.2f}")
    print("=" * 50)


if __name__ == "__main__":
    main()
