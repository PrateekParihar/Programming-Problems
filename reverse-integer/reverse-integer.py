class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x)
        
        reversedS = s[0] + s[1:][::-1] if s[0] == "-" else s[::-1]
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        result = int(reversedS)
        if result < INT_MIN or result > INT_MAX:
            return 0
        else:
            return result