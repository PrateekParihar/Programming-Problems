class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
            result = 0
            for num in nums:
                result ^= num
            return result
        
        
    '''
                    Basically what Bitwise exclusive OR (^) do is set same bits to zero (0^0=0 or 1^1=0) and different bits to one (0^1=1 or 1^0=1) .So when we do Bitwise exclusive OR (^) of same number we get 0. And in question we have frequency of every number is exactly except one ,so Bitwise exclusive OR (^) of every other number set to zero and whatever remains is our ans.
            Example [2,2,3,3,5]
            ans=2
            we start from index 1
            ans^2=0 ------->ans=0
            ans^3=3 ------->ans=3
            ans^3=0 ------->ans=0
            ans^5=5 ------->ans=5

            ans=5 is our answer
    '''