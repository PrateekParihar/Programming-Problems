class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
                                 ^ 
                [1,8,6,2,5,4,8,3,7]
                 ^              
        """
        
        start , end = 0 , len(height) - 1
        maxArea = 0
        
        while start < end:
            
            maxArea = max(maxArea, (end - start) * min(height[start], height[end]))
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            
        return maxArea
        