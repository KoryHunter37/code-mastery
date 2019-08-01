# https://app.codesignal.com/arcade/code-arcade/intro-gates/HEsmEacHr2s9wahjr

def maxMultiple(divisor: int, bound: int) -> int:
    for i in range(bound, 0, -1):
        if i % divisor == 0:
            return i
