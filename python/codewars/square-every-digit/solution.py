# https://www.codewars.com/kata/square-every-digit/train/python

def square_digits(num):
    return int(''.join(str(int(d) ** 2) for d in str(num)))
