# https://app.codesignal.com/arcade/code-arcade/intro-gates/aiKck9MwwAKyF8D4L

def lateRide(n: int) -> int:
    hours, minutes = map(str, divmod(n, 60))
    return sum(int(i) for i in hours + minutes)
