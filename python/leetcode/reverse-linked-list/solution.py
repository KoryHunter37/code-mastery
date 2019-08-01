# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        node = head
        nodes = [head]
        while(node.next):
            nodes.append(node.next)
            node = node.next
        
        for i in reversed(range(0, len(nodes))):
            if i == 0:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i-1]
        
        return nodes[len(nodes)-1]
            