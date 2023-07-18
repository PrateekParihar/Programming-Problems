class Solution:
    def myAtoi(self, s: str) -> int:
        
        res = ""
        startIdx = 0

        # remove leading whitespaces
        s = s.strip()

        # check if negative or positive
        if startIdx < len(s) and (s[startIdx] == "-" or s[startIdx] == "+"):
            res += s[startIdx]
            startIdx += 1

        # skip leading zeros
        while startIdx < len(s) and s[startIdx] == "0":
            startIdx += 1

        # convert digits to integer
        for i in range(startIdx, len(s)):
            if not s[i].isdigit():
                break
            res += s[i]

        # handle edge cases
        if len(res) == 0 or res == "+" or res == "-":
            return 0

        # clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        result = int(res)
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result
        
        
        