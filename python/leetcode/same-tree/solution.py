# https://leetcode.com/problems/same-tree/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        # Check this value
        if p.val == q.val:
            # Check left branch
            if p.left and q.left:
                if not self.isSameTree(p.left, q.left):
                    return False
            # If one has a left and the other does not
            elif p.left or q.left:
                return False
            
            # Check right branch
            if p.right and q.right:
                if not self.isSameTree(p.right, q.right):
                    return False
            # If one has a right and the other does not
            elif p.right or q.right:
                return False
        else:
            return False
        
        return True
                
                
                