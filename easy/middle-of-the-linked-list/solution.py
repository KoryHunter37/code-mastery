# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        i = 0
        D = {}
        D[i] = head
        
        curr_node = head
        while curr_node.next:
            i += 1
            curr_node = curr_node.next
            D[i] = curr_node
            
        half_index = math.ceil(float(i)/2)
        
        return D[half_index]