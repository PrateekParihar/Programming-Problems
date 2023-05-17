class Solution:
    def isValid(self, s: str) -> bool:
        
        keyMap = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []
        
        for ch in s:
            if ch in keyMap:
                stack.append(ch)
            elif len(stack) == 0 or ch != keyMap[stack.pop()]:
                return False

            
        return len(stack) == 0

#         stack = [] # only use append and pop
#         pairs = {
#             '(': ')',
#             '{': '}',
#             '[': ']'
#         }
#         for bracket in s:
#             if bracket in pairs:
#                 stack.append(bracket)
#             elif len(stack) == 0 or bracket != pairs[stack.pop()]:
#                 return False

#         return len(stack) == 0