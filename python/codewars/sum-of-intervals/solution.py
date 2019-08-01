# https://www.codewars.com/kata/sum-of-intervals/train/python

from itertools import chain

def sum_of_intervals(intervals):
    return len(set(chain(*[range(i[0], i[1]) for i in intervals])))
