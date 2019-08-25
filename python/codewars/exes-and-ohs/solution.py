# https://www.codewars.com/kata/exes-and-ohs/train/python

from collections import Counter

def xo(s):
    count = Counter(s.lower())
    
    return count.get('x') == count.get('o')