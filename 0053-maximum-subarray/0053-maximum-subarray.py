class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        res = max(res, sum)
           sum = 0
           
                              ^
         [-2,1,-3,4,-1,2,1,-5,4]
        
        sum += a[i] 
        if sum < 0 -> reset sum to 0 calculate again
        """
        
        res = nums[0]
        subSum = 0
        
        for num in nums:
            
            subSum += num
            res = max(res,subSum)        
            if subSum < 0:
                subSum = 0
                

            
        return res