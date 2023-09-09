class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        """
        [   0.  1.  2.  3.  4  
          0["1","1","1","1","0"],
          1["1","1","0","1","0"],
          2["1","1","0","0","0"],
          3["0","0","0","0","0"]
        ]
        
        
        (x,y) 
        top -> (x-1,y)
        bootom -> (x+1,y)
        left -> (x,y-1)
        right -> (x,y+1)
        
        """
        
        seen = set()
        
        res = 0
        
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r,c):
            
            # boundary coditions check + 1 check + seen check
            if (r not in range(rows) or c not in range(cols) or grid[r][c] != "1" or (r,c) in seen):
                return
            
            seen.add((r,c))
            
            bfs(r-1,c)
            bfs(r+1,c)
            bfs(r,c-1)
            bfs(r,c+1)
            
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == "1" and (r,c) not in seen:
                    res += 1
                    bfs(r,c)
                    
        return res