# https://www.codewars.com/kata/scramblies/train/python

from collections import Counter

def scramble(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    
    for key in c2.keys():
        if c2[key] > c1.get(key, 0):
            return False
            
    return True
    