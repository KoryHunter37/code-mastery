# https://www.codewars.com/kata/weight-for-weight/train/python

def order_weight(strng):
    arr = sorted(strng.split())
    
    arr = sorted( arr, key=lambda x: sum(int(digit) for digit in x) )
    return ' '.join(arr)

    