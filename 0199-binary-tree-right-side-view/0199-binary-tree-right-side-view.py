# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        """
            level order traversing 
            using a queue
            only append right node if there - Not valid if there is a right child in left subtree
            
            for level order - append right child first - only read first value at each level
        """
        if not root:
            return []
        
        res = []
        
        q = [root]
        
        while q:
            level = []
            
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

            res.append(level[0])
            
        return res
            