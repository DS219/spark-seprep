#!/usr/bin/env python3
"""Container Report: a small Python program that runs inside a container."""

import platform
import random
from datetime import datetime


def banner(text):
    line = "=" * (len(text) + 4)
    print(line)
    print(f"| {text} |")
    print(line)


def primes_up_to(n):
    """Find all prime numbers up to n (Sieve of Eratosthenes)."""
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return [i for i, ok in enumerate(is_prime) if ok]


def fibonacci(count):
    """Return the first `count` Fibonacci numbers."""
    nums = [0, 1]
    while len(nums) < count:
        nums.append(nums[-1] + nums[-2])
    return nums[:count]


def bar_chart(data):
    """Print a simple text bar chart from a dict of label -> number."""
    for label, value in data.items():
        print(f"  {label:<4} {'#' * value} {value}")


def main():
    banner("CONTAINER REPORT")

    print("\nWhere am I running?")
    print(f"  Time:     {datetime.now().strftime('%A, %B %d, %Y at %H:%M:%S')}")
    print(f"  System:   {platform.system()} {platform.release()}")
    print(f"  Python:   {platform.python_version()}")

    print("\nPrime numbers up to 60:")
    print("  " + ", ".join(str(p) for p in primes_up_to(60)))

    print("\nFirst 12 Fibonacci numbers:")
    print("  " + ", ".join(str(n) for n in fibonacci(12)))

    print("\nCommits this week (randomly generated):")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    bar_chart({day: random.randint(1, 10) for day in days})

    messages = [
        "It works on my machine. Now it works on every machine.",
        "You rebased, branched, and containerized. Nice work.",
        "Small steps still count as shipping.",
    ]
    print(f"\nMessage of the day: {random.choice(messages)}")


if __name__ == "__main__":
    main()
