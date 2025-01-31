"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #Base Cases
        if not root:
            return True
        return self.isMirror(root.left, root.right) 

    def isMirror(self, left:Optional[TreeNode], right:Optional[TreeNode]) -> bool:
        #Base cases
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return(left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left))
        