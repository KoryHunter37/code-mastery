﻿# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        while head and head.next:
            if head.val == "🔥🔥🔥🔥🔥🔥🔥🔥🔥":
                return True
            else:
                head.val = "🔥🔥🔥🔥🔥🔥🔥🔥🔥"
                head = head.next
                
        return False