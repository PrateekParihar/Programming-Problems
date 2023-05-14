class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        track = {}

        for num in nums:
            if num in track:
                return True
            else:
                track[num] = True
                
        return False