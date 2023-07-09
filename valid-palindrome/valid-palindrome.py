class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        - Clean string - regex or any other ways
        - Check edge cases
        - Two pointer one input pattern
        """
        cleanedStr = (re.sub( r"[^A-Za-z0-9]","",s )).lower()
        
        if not cleanedStr:
            return True
        
        left = 0
        right = len(cleanedStr) -1
        
        while left < right:
            if cleanedStr[left] != cleanedStr[right]:
                return False
            left += 1
            right -= 1
            
        return True