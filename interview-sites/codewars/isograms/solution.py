# https://www.codewars.com/kata/isograms/train/python

def is_isogram(string):
    return len(string) == len(set(string.lower()))
