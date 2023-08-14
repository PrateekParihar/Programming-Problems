class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # sort
        
        nums.sort()
        
        # loop and check if nums[i] !== nums[i+1] - 1
        
        for i in range(len(nums) -1):
            
            if nums[i] +1 != nums[i+1]:
                return nums[i] + 1
            
        return nums[-1] + 1 if nums[0] == 0 else 0
        