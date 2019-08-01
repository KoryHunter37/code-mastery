# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/QrCSNQWhnQoaK9KgK

def arithmeticExpression(a: int, b: int, c: int) -> bool:
    return any([a+b==c, a-b==c, a*b==c, a/b==c])
