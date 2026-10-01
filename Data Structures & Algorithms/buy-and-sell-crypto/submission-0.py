class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        #max_profit 0

        for n in prices :
            min_price = min (n,min_price)
            max_profit = max(n - min_price, max_profit ) #4

        return max_profit
            
