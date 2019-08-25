# https://www.codewars.com/kata/numerical-palindrome-number-1/train/python

def palindrome(num):
    if type(num) is not int or num < 0:
        return 'Not valid'
    return str(num) == str(num)[::-1]
