#!/usr/bin/env python3
# A little demo script: prints a greeting plus a sample LeetCode result.

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

if __name__ == "__main__":
    print("Hello from inside the container!")
    example = [7, 1, 5, 3, 6, 4]
    print(f"Sample max_profit({example}) →", max_profit(example))
