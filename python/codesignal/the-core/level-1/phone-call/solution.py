# https://app.codesignal.com/arcade/code-arcade/intro-gates/mZAucMXhNMmT7JWta

def phoneCall(min1: int, min2_10: int, min11: int, s: int) -> int:
    
    if s < min1:
        return 0
    elif s == min1:
        return 1
    elif min2_10 <= s - min1 <= min2_10 * 9:
        return (s - min1) // min2_10 + 1
    else:
        return (s - min1 - min2_10 * 9) // min11 + 10
     