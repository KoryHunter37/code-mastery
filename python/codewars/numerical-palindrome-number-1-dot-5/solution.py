# https://www.codewars.com/kata/numerical-palindrome-number-1-dot-5/train/python

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome(num,s):
    def is_valid_input(i):
        try:
            assert type(i) is int
            assert i >= 0
        except AssertionError:
            return False
        return True

    if not is_valid_input(num) or not is_valid_input(s):
        return 'Not valid'

    result = []
    
    while len(result) < s:
        if num >= 10 and is_palindrome(num):
            result.append(num)
        
        num += 1
        
    return result
