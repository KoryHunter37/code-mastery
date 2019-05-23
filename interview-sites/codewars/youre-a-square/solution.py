# https://www.codewars.com/kata/youre-a-square/train/python

from math import sqrt

def is_square(n):    
    return n == 0 or n >= 0 and float(sqrt(n)).is_integer()
