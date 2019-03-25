# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/sgDWKCFQHHi5D3Szj

from collections import Counter

def extraNumber(a: int, b: int, c: int) -> int:
    return sorted(Counter((a, b, c)).items(), key=lambda e: e[1])[0][0]
