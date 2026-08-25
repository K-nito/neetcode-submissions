class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = 101
        i = 0

        while i < len(prices) - 1:
            i += 1
            minBuy = min(minBuy, prices[i - 1])
            profit = max(profit, prices[i] - minBuy)

        return profit