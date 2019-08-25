# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l3 = None
        root = []
        
        while l1 is not None or l2 is not None:
            best = None
            if l1 is not None and l2 is None:
                best = l1
                l1 = l1.next
            elif l1 is None and l2 is not None:
                best = l2
                l2 = l2.next
            elif l1.val <= l2.val:
                best = l1
                l1 = l1.next
            else:
                best = l2
                l2 = l2.next
                
            if l3 is None:
                l3 = best
                root = l3
            else:
                l3.next = best
                l3 = l3.next
        
        return root
