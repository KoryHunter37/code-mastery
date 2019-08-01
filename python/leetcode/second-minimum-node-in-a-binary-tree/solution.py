# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode, base=True) -> int:
        
        if root.left is None:
            if base:
                return -1
            return [root.val]
        elif base:
            result = sorted(set([root.val] + self.findSecondMinimumValue(root.left, False) + self.findSecondMinimumValue(root.right, False)))
            try:
                return result[1]
            except:
                return -1           
        else:
            return [root.val] + self.findSecondMinimumValue(root.left, False) + self.findSecondMinimumValue(root.right, False)
            