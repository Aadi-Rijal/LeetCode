class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = False
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1] and not buy:
                buy = True
                bp = prices[i]
            elif prices[i] > prices[i + 1] and buy:
                    profit += prices[i] - bp
                    buy = False
        if buy:
            profit += prices[i + 1] - bp
        return profit