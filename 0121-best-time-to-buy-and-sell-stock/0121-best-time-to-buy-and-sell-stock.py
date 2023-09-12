class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            *
            7,1,5,3,6,4
        
        """
        
        lowest = prices[0]
        
        profit = 0
        
        for price in prices:
            
            if price < lowest:
                lowest = price
                
            profit = max(profit,price-lowest)
            
        
        return profit