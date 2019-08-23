# https://www.codewars.com/kata/give-me-a-diamond/train/python

from collections import deque

def diamond(n):

    # Return None if the input is an even number or negative, as it is not possible
    # to print a diamond of even or negative size.
    if n %2 == 0 or n < 0:
        return None
    
    diamond_string = deque()
    stars = n
            
    while stars >= 1:
        next = ' ' * ((n - stars)//2) + '*' * stars + '\n'
        
        if len(diamond_string) > 0:
            diamond_string.appendleft(next)
        diamond_string.append(next)  
            
        stars -= 2
        
    return ''.join(diamond_string)
