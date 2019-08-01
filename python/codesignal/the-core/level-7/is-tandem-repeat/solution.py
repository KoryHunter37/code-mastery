# https://app.codesignal.com/arcade/code-arcade/book-market/2SDWWyHY9Xw5CpphY

def isTandemRepeat(s: str) -> bool:
    return s[:len(s)//2] == s[len(s)//2:]
