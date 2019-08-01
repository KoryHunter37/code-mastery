# https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm

from typing import Type

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l: Type[ListNode], k: int):
    # Empty Input List Only
    if l is None:
        return []
    
    root = l
    while l.next is not None:
        if l.next.value == k:
            l.next = l.next.next
            
        else:
            l = l.next
         
    return root if root.value != k else root.next
