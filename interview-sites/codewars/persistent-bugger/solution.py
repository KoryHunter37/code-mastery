# https://www.codewars.com/kata/persistent-bugger/train/python

from functools import reduce

def persistence(n):
    depth = 0
    
    while len(str(n)) > 1:
        depth += 1
        n = reduce( lambda x, y: str(int(x) * int(y)), str(n))
        n = ''.join(n)
        
    return depth
