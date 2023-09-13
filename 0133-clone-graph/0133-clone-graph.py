"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        """
        [[2,4],[1,3],[2,4],[1,3]]
        
        { 
            1: 
            2: 
            3:
            4:
        }
        
        
        
        """
        track = {}
        
        def dfs(node):
            
            if node in track:
                return track[node]
            
            copy = Node(node.val)
            track[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy
        
        return dfs(node) if node else None