class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)-1):
                max_rest = max(prices[i+1:])
                profit = max_rest-prices[i]
                max_profit = max(profit, max_profit)

        return max_profit