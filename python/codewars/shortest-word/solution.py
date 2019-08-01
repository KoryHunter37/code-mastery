# https://www.codewars.com/kata/shortest-word/train/python

def find_short(s):
    return min([len(word) for word in s.split()])