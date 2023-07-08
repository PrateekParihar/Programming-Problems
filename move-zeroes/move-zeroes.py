class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        - Two pointer approach
        - One for traverse array
        - Other to track the position of 0
        """
        
        p = None
        
        for i in range(len(nums)):
            
            if p is None and nums[i] == 0:
                p = i
            else:
                if p is not None and nums[i] != 0:
                    nums[p] = nums[i]
                    nums[i] = 0
                    p += 1

