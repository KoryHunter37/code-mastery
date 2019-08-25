# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/aFF9HDm2Rsti9j5kc

def isInfiniteProcess(a: int, b: int) -> bool:
    if a == b:
        return False
    elif abs(a - b) % 2 == 0:
        return a+1 > b-1
    return True
