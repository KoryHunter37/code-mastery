# https://www.codewars.com/kata/maximum-subarray-sum/train/python

def maxSequence(arr):
    prev = None
    mx = None
    
    for e in arr:
        if prev is None:
            prev = e
        elif e + prev <= e:
            prev = e
        else:
            prev = e + prev
            
        if mx is None or prev > mx:
            mx = prev
        
    if mx is None:
        return 0
    return max(mx, 0)
