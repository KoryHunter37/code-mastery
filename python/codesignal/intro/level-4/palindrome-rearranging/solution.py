# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico

from collections import Counter

def palindromeRearranging(inputString):
    count = Counter(inputString)
    
    odd_nums = 0
    for c in count.values():
        if c % 2 == 1:
            odd_nums += 1
            
        if odd_nums > 1:
            return False
        
    return True