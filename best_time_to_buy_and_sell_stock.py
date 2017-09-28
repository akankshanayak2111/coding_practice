class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
            
        return max_profit
        