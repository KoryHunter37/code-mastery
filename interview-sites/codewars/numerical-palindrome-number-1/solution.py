# https://www.codewars.com/kata/numerical-palindrome-number-1/train/python

def palindrome(num):
    if type(num) is not int or num < 0:
        return 'Not valid'

    s = str(num)
    return s[:len(s)//2] == s[:len(s)-len(s)//2-1:-1]
