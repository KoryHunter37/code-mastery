# https://www.codewars.com/kata/anagram-detection/train/python

from collections import Counter

def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())
