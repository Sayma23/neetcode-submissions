class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range (0, len(prices) -1):
            buy = min (buy, prices[i])
            profit = max (profit, prices[i+1] - buy)
            print(profit)
        return 0 if profit < 1 else profit


        