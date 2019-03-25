# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/b5z4P2r2CGCtf8HCR

def killKthBit(n, k):
    return int(str(bin(n)[:len(bin(n)) - k] + '0' + bin(n)[len(bin(n)) - k + 1:]).replace('b', ''), 2)
