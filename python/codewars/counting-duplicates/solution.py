# https://www.codewars.com/kata/counting-duplicates/train/python

from collections import Counter

def duplicate_count(text):
    c = Counter(text.upper())
    return sum(1 for v in c.values() if v > 1)
