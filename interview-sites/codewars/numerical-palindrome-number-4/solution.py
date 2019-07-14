# https://www.codewars.com/kata/numerical-palindrome-number-4/train/python

def is_palindrome(num):
    if num < 10:
        return False
        
    s = str(num)
    return s[0:len(s)//2] == s[len(s)-1:len(s)-len(s)//2-1:-1]

def palindrome(num):
    if type(num) is not int or num < 0:
        return 'Not valid'
    
    if is_palindrome(num):
        return num
    
    n = 1
    while True:
        if is_palindrome(num + n):
            return num + n
        elif is_palindrome(num - n):
            return num - n
        n += 1
