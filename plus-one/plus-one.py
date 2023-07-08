class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        - Reverse
        - Loop
            - add +1
            - handle 10
        - return reverse 
        '''
        
        digits.reverse()

        carry = 1
        for i in range(len(digits)):
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum // 10

        if carry > 0:
            digits.append(carry)

        digits.reverse()
        return digits
            