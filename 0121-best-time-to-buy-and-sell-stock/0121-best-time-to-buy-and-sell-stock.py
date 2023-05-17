class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ptr1=0
        ptr2=0
        
        profit = 0
        
        while ptr2 < len(prices):
            if profit < prices[ptr2] - prices[ptr1]:
                profit = prices[ptr2] - prices[ptr1]
                
            if prices[ptr2] < prices[ptr1]:
                ptr1 = ptr2
                
            ptr2 += 1
            
        return profit
        