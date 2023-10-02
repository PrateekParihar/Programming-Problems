class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            
              ^
                 *
            "AABABBAA"  k=1
        
        - sliding window
        - use char with max occurance for update
        - keep track of k
        """
        
        longestS = 0
        
        p1 = 0
        trackMax = collections.defaultdict(int)
        
        for p2 in range(len(s)):

            trackMax[s[p2]] += 1
            maxVal = max(trackMax.values())

            while (p2 - p1 + 1) - maxVal > k:
                trackMax[s[p1]] -= 1
                p1 += 1
                
            longestS = max(longestS, (p2 - p1 + 1))
        
        return longestS
            
            