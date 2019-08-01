# https://www.codewars.com/kata/moving-zeros-to-the-end/train/python

from typing import List

def move_zeros(array: List) -> List:
    new_array = [e for e in array if e != 0 or e is False]
    
    zero_count = len(array) - len(new_array)
    return new_array + [0] * zero_count
