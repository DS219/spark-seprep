# Jonathan Tsang

Hi, my name is Jonathan Tsang and my favorite programming language is Python. I like it because the syntax is clean and you can go from an idea to a working script really quickly without a lot of boilerplate.

## Example code

```python
def best_time_to_buy_sell(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(best_time_to_buy_sell(prices))
```

### Code Explanation

This script solves the "Best Time to Buy and Sell Stock" problem. It tracks the lowest price seen so far and the best profit possible at each step. To run it, save the file as `stocks.py` and run `python3 stocks.py` in your terminal. It should print `5`.
