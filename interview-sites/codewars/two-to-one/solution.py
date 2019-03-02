# https://www.codewars.com/kata/two-to-one/train/python

def longest(s1, s2):
    return "".join(sorted(list(set(s1) | set(s2))))