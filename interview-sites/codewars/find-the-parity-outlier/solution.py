# https://www.codewars.com/kata/find-the-parity-outlier/train/python

def find_outlier(integers):
    
    evens = 0
    first_even = None
    odds = 0
    first_odd = None

    for i in integers:
    
        if i % 2 == 0:
            if odds > 1:
                return i
            else:
                evens += 1
                if not first_even:
                    first_even = i
                
        else:
            if evens > 1:
                return i
            else:
                odds += 1
                if not first_odd:
                    first_odd = i
                    
    if evens > odds:
        return first_odd
    else:
        return first_even
    