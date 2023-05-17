class Solution {
    public int maxProfit(int[] prices) {
        
        int ptr1 =0;
        int ptr2 =0;
        
        int profit =0;
        
        while(ptr2 < prices.length){
            
            if(profit < (prices[ptr2] - prices[ptr1])){
                profit = prices[ptr2] - prices[ptr1];
            }
            
            if(prices[ptr2] < prices[ptr1]){
                ptr1=ptr2;
            }
            

            
            ptr2 += 1;
        }
        
        return profit;
    }
}