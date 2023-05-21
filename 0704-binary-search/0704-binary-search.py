class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return nums
        
        L = 0
        R = len(nums) -1
        
        while R >= L :
            
            M = (R + L) // 2
            
            if target > nums[M]:
                L = M +1
            else:
                R = M -1
                
            if target == nums[M]:
                return M
            
        return -1
            