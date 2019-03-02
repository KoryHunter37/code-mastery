# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def traverse(node, depth):
            if not node:
                return 0
            left_depth = depth
            right_depth = depth
            if node.left:
                left_depth = traverse(node.left, depth+1)
            if node.right:
                right_depth = traverse(node.right, depth+1)
                
            return max(left_depth, right_depth)
        
        
        return traverse(root, 1)