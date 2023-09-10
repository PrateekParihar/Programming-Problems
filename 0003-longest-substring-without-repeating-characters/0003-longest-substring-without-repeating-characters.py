class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """       ^
                "abcabcbb"
                     ^
        r = 1
               ^
             "aab"
                ^
        
        """
        
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1        
        
        res = 0
        
        p1 = 0
        
        for p2 in range(len(s)):
            
            while p1!=p2 and s[p2] in s[p1:p2]:
                p1+= 1

            res = max(res, p2-p1+1)
            

        return res
            
            