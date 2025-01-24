"""
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        #Base Cases 
        while stack:
            node_p, node_q = stack.pop()

            if not node_p and not node_q:
                continue
            
            if None in (node_p, node_q):
                return False
            
            if node_p.val != node_q.val:
                return False
            
            stack.append((node_p.right, node_q.right))
            stack.append((node_p.left, node_q.left))
        return True
