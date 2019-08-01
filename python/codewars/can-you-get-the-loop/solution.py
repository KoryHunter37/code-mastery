# https://www.codewars.com/kata/can-you-get-the-loop/train/python

def loop_size(node):
      slow_ptr = node
      fast_ptr = node
      
      while True:
          slow_ptr = slow_ptr.next
          fast_ptr = fast_ptr.next.next
          
          if slow_ptr == fast_ptr:
              break
      
      fast_ptr = fast_ptr.next
      length = 1

      while slow_ptr != fast_ptr:
          fast_ptr = fast_ptr.next
          length += 1
          
      return length