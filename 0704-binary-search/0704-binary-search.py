class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return nums
        
        L = 0
        R = len(nums) -1
        
        while R >= L :
            
            M = L + (R-L) // 2  # (l + r) // 2 can lead to overflow
            
            if target > nums[M]:
                L = M +1
            else:
                R = M -1
                
            if target == nums[M]:
                return M
            
        return -1
            