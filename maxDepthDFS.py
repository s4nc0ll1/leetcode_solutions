'''
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Base Case
        if not root:
            return 0

        stack =  [(root,1)]
        max_depth = 0 
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(depth, max_depth)
                stack.append((node.right, depth + 1))
                stack.append((node.left, depth + 1))

        return max_depth
                

