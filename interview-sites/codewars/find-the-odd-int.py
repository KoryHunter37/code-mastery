# https://www.codewars.com/kata/find-the-odd-int/train/python

from collections import Counter

def find_it(seq):
    count = Counter(seq)
    odd_count = [item[0] for item in count.items() if item[1] % 2 == 1]
    return odd_count[0]
