# https://app.codesignal.com/arcade/intro/level-10/ppZ9zSufpjyzAsSEx

def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def buildPalindrome(s: str) -> str:
    if is_palindrome(s):
        return s
    
    for i, letter in enumerate(s):
        curr = s + s[i::-1]
        if is_palindrome(curr):
            return curr      
