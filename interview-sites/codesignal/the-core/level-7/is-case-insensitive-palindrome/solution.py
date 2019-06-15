# https://app.codesignal.com/arcade/code-arcade/book-market/G9wj2j6zaWwFWsise

def isCaseInsensitivePalindrome(s: str) -> bool:
    first_half, second_half = s[:len(s)//2], s[-(len(s)//2):]
    return first_half.lower() == second_half[::-1].lower()
