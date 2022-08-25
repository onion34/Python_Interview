# Python Interview
# Best Time to Buy and Sell Stock / p.195
# parameter prices: list[int]
# return: int

def solution_by_brute_force(prices):
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


def solution_by_kadane_algorithm(prices):
    import sys

    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit
