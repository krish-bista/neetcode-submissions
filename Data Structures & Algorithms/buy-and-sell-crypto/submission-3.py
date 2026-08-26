class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 100000000000
        sell = 0
        maxProfit = 0
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
                sell = 0

            elif price > sell:
                sell = price
            profit = sell - buy
            maxProfit = max(maxProfit, profit)
        
        if maxProfit < 0:
            return 0
        return maxProfit