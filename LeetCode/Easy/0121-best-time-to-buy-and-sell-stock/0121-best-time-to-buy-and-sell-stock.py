class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        profit = 0
        for sp in prices:
            if sp < bp:
                bp = sp
            elif sp - bp > profit:
                profit = sp - bp
        return profit