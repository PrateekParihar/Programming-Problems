# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if self.isSameTree(root,subRoot):
            return True
        
        if root.left and self.isSubtree(root.left,subRoot):
            return True
             
        if root.right and self.isSubtree(root.right, subRoot):
            return True

        return False
        
        
    def isSameTree(self,p,q):
        # Edge case / Base case
        if p is None and q is None:
            return True
        
        if (p == None and q != None) or (p != None and q == None):
            return False
        
        if p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        
        return False
        