# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


def maxProfit(prices):
    hold = 0
    profit = 0
    buy_price = 0

    for i in range(len(prices) - 1):
        if hold == 0 and prices[i + 1] >= prices[i]:
            hold = 1
            buy_price = prices[i]
        elif hold == 1 and prices[i + 1] < prices[i]:
            hold = 0
            profit += prices[i] - buy_price
            buy_price = 0

    if hold:
        profit += prices[len(prices) - 1] - buy_price

    return profit


if __name__ == "__main__":
    print(maxProfit([7, 6, 4, 3, 1]))
