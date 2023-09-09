class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        """
            [r*c]
            pacific ocean boundary - [0,c] [r,0]
            atlantic ocean boundary - [len(r) -1,c] [r,len(c) -1]            
        
        """
        
        rows, cols = len(heights), len(heights[0])
        
        pac, alt = set(), set()  # which can reach to these oceans
        
        res = []
        
        
        def dfs(r,c,height, seen):
            
            if r not in range(rows) or c not in range(cols) or heights[r][c] < height or (r,c) in seen:
                return
            seen.add((r,c))
            
            dfs(r+1,c,heights[r][c], seen)
            dfs(r-1,c,heights[r][c], seen)
            dfs(r,c+1,heights[r][c], seen)
            dfs(r,c-1,heights[r][c], seen)
            
        
        for c in range(cols):
                dfs(0,c,heights[0][c], pac)
                
                dfs(rows-1,c, heights[rows-1][c], alt)
                
                
        for r in range(rows):
                dfs(r,0,heights[r][0], pac)
                dfs(r,cols-1, heights[r][cols-1], alt)
                
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in alt:
                    res.append([r,c])
                    
        return res
                