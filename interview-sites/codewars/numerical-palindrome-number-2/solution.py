# https://www.codewars.com/kata/numerical-palindrome-number-2/train/python

def is_palindrome(s):
    return s == s[::-1]

def palindrome(num):
    if type(num) is not int or num < 0:
        return 'Not valid'
    
    s = str(num)
    
    for length in range(2, len(s)+1):
        for i in range(0, len(s)+1 - length):
            if is_palindrome(s[i:i+length]):
                return True
                
    return False
