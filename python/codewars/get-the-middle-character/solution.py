# https://www.codewars.com/kata/get-the-middle-character/train/python

def get_middle(s):
    length = len(s)
    
    if length % 2 == 1:
        return s[(length - 1)/2]
    else:
        return s[length/2 - 1: length/2 + 1]
