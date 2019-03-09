# https://www.codewars.com/kata/bit-counting/train/python

def countBits(n):
    return str(bin(n)).count("1")
    