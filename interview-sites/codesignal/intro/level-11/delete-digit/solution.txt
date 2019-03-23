# https://app.codesignal.com/arcade/intro/level-11/vpfeqDwGZSzYNm2uX

def deleteDigit(n: int) -> int:
    n = str(n)
    return max( int(n[:i] + n[i+1:]) for i in range(len(n)) )
