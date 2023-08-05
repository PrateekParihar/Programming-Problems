class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        nums.sort()
        
        for i, val in enumerate(nums):
            
            if nums[i] > 0:
                break
                
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            # two sum problem
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                if nums[j] + nums[k] + nums[i] < 0 :
                    j += 1
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    
        return res