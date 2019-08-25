# https://app.codesignal.com/arcade/intro/level-10/PHSQhLEw3K2CmhhXE

from collections import Counter
from string import ascii_lowercase

def isBeautifulString(s: str) -> bool:
    count = Counter(s)

    last = float('inf')
    for letter in ascii_lowercase:
        curr = count.get(letter, 0)
        
        if curr > last:
            return False
        
        last = curr
        
    return True
