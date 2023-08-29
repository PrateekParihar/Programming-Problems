# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = []
        result = []
        
        if root is None:
            return []
        
        queue.append(root)
        
        
        while queue:
            leaves = []
            
            for i in range (len(queue)):
                node = queue.pop(0)
                leaves.append(node.val)
                
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                    
            if len(leaves) > 0:   
                result.append(leaves)
            
        return result
            
            
            
            
            