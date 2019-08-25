# https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i1 = []
        while(l1.next is not None):
            i1.append(l1.val)
            l1 = l1.next
        i1.append(l1.val)
        
        i2 = []
        while(l2.next is not None):
            i2.append(l2.val)
            l2 = l2.next
        i2.append(l2.val)
            
        i1 = i1[::-1]
        i2 = i2[::-1]
        i1 = int("".join(map(str, i1))) 
        i2 = int("".join(map(str, i2))) 
        
        result = str(i1 + i2)[::-1]
        
        root = ListNode(result[0])
        curr = root
        for d in range(1, len(result)):
            curr.next = ListNode(result[d])
            curr = curr.next
        return root