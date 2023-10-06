class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
          ^
         [2,7,11,15]
            *
        """
        
        start, end = 0, len(numbers) - 1
        
        while end > start:
            
            if numbers[end] + numbers[start] > target:
                end -= 1
            elif numbers[end] + numbers[start] < target:
                start += 1
            else:
                return [start+1,end+1]
            
        