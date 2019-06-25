# https://www.codewars.com/kata/find-the-next-perfect-square/train/python

from math import sqrt

def find_next_square(sq):
    squared = sqrt(sq)
    if squared.is_integer():
        return (squared + 1) ** 2
    return -1
