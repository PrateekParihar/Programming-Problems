class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        - Sol1- Sort both strings and compare
        - Sol2- use dict to track charater occrance
        - Sol3 - Use of The Counter class from the collections module 
        """
        
        if len(s) != len(t):
            return False
        
        # if ''.join(sorted(s)) != ''.join(sorted(t)):
        #     return False
        
        # return True
        
        tracker = {}
        
        for ch in s:
            tracker[ch] = tracker.get(ch, 0) + 1
            
        for ch in t:
            if ch not in tracker:
                return False
            else:
                tracker[ch] -= 1
                
        for val in tracker.values():
            if val > 0 :
                return False
        
        return True
            