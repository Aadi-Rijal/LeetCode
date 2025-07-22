class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy]
            if profit <= 0:
                buy = sell
            max_profit = max(profit, max_profit)
        return max_profit
        