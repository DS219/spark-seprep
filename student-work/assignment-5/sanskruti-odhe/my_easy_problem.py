# LeetCode Problem: Best Time to Buy and Sell Stock (121)
# Given an array prices where prices[i] is the price of a given stock on day i,
# return the maximum profit you can achieve. You may complete at most one transaction
# (i.e., buy one and sell one share of the stock).
# Constraints:
#   1 <= prices.length <= 10**5
#   0 <= prices[i] <= 10**4

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        # update the minimum price so far
        if price < min_price:
            min_price = price
        # compute profit if sold today
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

if __name__ == "__main__":
    # Example tests
    print(max_profit([7, 1, 5, 3, 6, 4]))  # expected 5
    print(max_profit([7, 6, 4, 3, 1]))     # expected 0
