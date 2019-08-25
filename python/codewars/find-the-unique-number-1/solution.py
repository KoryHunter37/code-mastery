# https://www.codewars.com/kata/find-the-unique-number-1/train/python

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) < arr.count(b) else b