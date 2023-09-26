class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # DP tabulation solution
        table = [[0 for col in range(n+1)] for row in range(m+1)]
        
        table[1][1] = 1
        
        for row in range(m+1):
            for col in range(n+1):
                if row +1 <= m:
                    table[row+1][col] += table[row][col]
                if col +1 <= n:
                    table[row][col+1] += table[row][col]
                    
        return table[m][n]
                
        
        
#         # DP memoization soltion
        
#         if (m,n) in memo.keys():
#             return memo[(m,n)]
        
#         if m == 0 or n == 0:
#             return 0
        
#         if m == 1 and n == 1:
#             return 1
        
        
#         memo[(m,n)] = self.uniquePaths(m-1,n, memo) + self.uniquePaths(m,n-1, memo)
        
#         return memo[(m,n)]



        