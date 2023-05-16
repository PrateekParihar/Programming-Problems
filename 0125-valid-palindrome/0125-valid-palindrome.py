class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        filterStr = re.sub(r"[^A-Za-z0-9]", "", s)
        
        if not filterStr:
            return True
        
        length = len(filterStr)
        
        ptr1 = length // 2 - 1
        ptr2 = length // 2 if length % 2 == 0 else length // 2 + 1
        
        
        while(ptr1 >= 0 and ptr2 < length):
            
            if filterStr[ptr1].lower() != filterStr[ptr2].lower():
                return False
            
            ptr1 -= 1
            ptr2 += 1
            
            
        return True
            
        
        