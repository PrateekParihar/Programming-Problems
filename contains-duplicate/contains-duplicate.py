class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        - track the value in seen map or seen set
        '''
        seen = {}
        
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
            
        return False
        