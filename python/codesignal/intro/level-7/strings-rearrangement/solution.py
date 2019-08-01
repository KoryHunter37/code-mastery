# https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9

from typing import List

def one_letter_difference(s1: str, s2: str) -> bool:
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
            
        if diff > 1:
            return False
        
    return diff == 1


def stringsRearrangement(arr: List[str], last: str=None) -> bool:
    # Final Case
    if len(arr) == 0:
        return True
    
    # Initial Case
    elif last is None:
        for i in range(len(arr)):
            if stringsRearrangement(arr[0:i] + arr[i+1:], arr[i]): return True
    
    # Intermediary Cases              
    else:
        for i, s in enumerate(arr):
            if one_letter_difference(last, s):
                if stringsRearrangement(arr[0:i] + arr[i+1:], s): return True
                
    return False
