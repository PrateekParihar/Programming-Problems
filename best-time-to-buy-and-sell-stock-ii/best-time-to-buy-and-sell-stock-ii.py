class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        - Sliding Window approach
        - Sum of profits
        '''

        maxProfit = buy = 0
        
        for sell in range(1, len(prices)):  #starting from 1 as only one price cannot sell
            if prices[buy] > prices[sell]:
                buy += 1
            else:
                maxProfit += prices[sell] - prices[buy]
                buy = sell
                
        return maxProfit