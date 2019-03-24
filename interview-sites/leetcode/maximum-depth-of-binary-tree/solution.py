# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode, depth: int = 1) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return depth
        elif root.left is None:
            return self.maxDepth(root.right, depth+1)
        elif root.right is None:
            return self.maxDepth(root.left, depth+1)
        else:
            return max(self.maxDepth(root.left, depth+1), self.maxDepth(root.right, depth+1))
