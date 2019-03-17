# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32

from collections import Counter
import string

def commonCharacterCount(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    count = 0
    for letter in string.ascii_lowercase:
        count += min(c1.get(letter, 0), c2.get(letter, 0))
    
    return count
