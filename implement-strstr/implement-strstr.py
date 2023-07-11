class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        - Two pointer two input pattern
        - exhaust both until condition matched
        - handle half match scenario and edge cases
        """
        
        p1 = p2 = 0
        
        while p1 < len(haystack):
            
            if haystack[p1] == needle[p2]:
                if p2 == len(needle) -1 :
                    return p1 - p2
                p2 += 1
            else:
                p1 -= p2  # reset p1 if half match found
                p2 = 0
                
            p1 += 1
        
        return -1
            
        