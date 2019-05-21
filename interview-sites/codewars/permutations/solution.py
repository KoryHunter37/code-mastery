# https://www.codewars.com/kata/permutations/train/python

from itertools import permutations as p

def permutations(string):
    return [''.join(e) for e in list(set(p(string)))]
