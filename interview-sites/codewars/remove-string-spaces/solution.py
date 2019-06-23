# https://www.codewars.com/kata/remove-string-spaces/train/python

def no_space(x):
    return x.translate(str.maketrans({' ': ''}))
