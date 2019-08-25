# https://www.codewars.com/kata/even-or-odd/train/python

def even_or_odd(number):
    return {0:"Even", 1:"Odd"}.get(number%2)
    