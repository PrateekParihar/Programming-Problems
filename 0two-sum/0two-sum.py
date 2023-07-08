class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        
        for i, val in enumerate(nums):
            if target - val in seen:
                result = [i , seen[target - val] ]
                return result
            seen[val] = i
            
        return []
            
        
        