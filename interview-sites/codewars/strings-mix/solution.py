# https://www.codewars.com/kata/strings-mix/train/python

from collections import Counter
from string import ascii_lowercase

def mix(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    letters = set(s1 + s2) & set(ascii_lowercase)
    
    result = {}
    
    for letter in letters:
        c1_count = c1.get(letter, 0)
        c2_count = c2.get(letter, 0)
        
        # Must be strictly greater than 1
        if c1_count <= 1 and c2_count <= 1:
            continue
        
        if c1_count > c2_count:
            result[letter] = '1:' + letter * c1_count
        elif c1_count < c2_count:
            result[letter] = '2:' + letter * c2_count
        else:
            result[letter] = '=:' + letter * c1_count
        
    
    final_result = []
    
    print(result.values())
    for item in sorted(sorted(result.values()), key=len, reverse=True):
        final_result.append(item)
        
    return '/'.join(final_result)