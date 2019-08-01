# https://www.codewars.com/kata/twice-linear/train/python

import itertools
from collections import deque

def dbl_linear(n):
    
    def u_gen():
        curr = 1
        slow = deque()
        fast = deque()
        
        while True:        
            yield curr
            y = 2 * curr + 1
            z = 3 * curr + 1
            
            slow.append(y)
            fast.append(z)
            
            if slow[0] < fast[0]:
                curr = slow.popleft()
            elif fast[0] < slow[0]:
                curr = fast.popleft()
            else:
                curr = slow.popleft()
                fast.popleft()
            
    print(list(itertools.islice(u_gen(), 0, 31))) 
    return list(itertools.islice(u_gen(), n, n+1))[0]
