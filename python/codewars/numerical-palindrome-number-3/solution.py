# https://www.codewars.com/kata/numerical-palindrome-number-3/train/python

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome(num):
    def _is_valid_input(i):
        return type(i) is int and i >= 0

    if not _is_valid_input(num):
        return 'Not valid'

    palindromes = 0
    s = str(num)
    
    for length in range(2, len(s)+1):
        for i in range(0, len(s)-length+1):
            if is_palindrome(s[i:i+length]):
                palindromes += 1
        
    return palindromes