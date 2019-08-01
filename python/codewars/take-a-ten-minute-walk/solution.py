# https://www.codewars.com/kata/take-a-ten-minute-walk/train/python

from collections import Counter

def isValidWalk(walk):

    # Walk must take exactly 10 minutes.
    if len(walk) != 10:
        return False
    
    # Count the number of occurences of each direction.   
    occurences = Counter(walk)
    
    # If each direction occurred the same number of times as its counterpart, then the walk has returned to the start.
    return occurences.get('n', 0) == occurences.get('s', 0) and occurences.get('e', 0) == occurences.get('w', 0)
