class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        """
                1,2,3,4
                
                1,1,8,6
                
        """
        
        res = [1] * len(nums)
        res2 = [1] * len(nums)
        
        for i in range(1,len(res)):        
            res[i] = nums[i-1] * res[i-1]
            
        for i in range(len(res)-2,-1,-1):
            res2[i] = res2[i+1] * nums[i+1] 
            
        for i in range(len(res)):
            res[i] = res[i] * res2[i]
            
            
        return res
            
            
            