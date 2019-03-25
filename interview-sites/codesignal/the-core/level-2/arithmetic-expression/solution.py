# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/QrCSNQWhnQoaK9KgK

def arithmeticExpression(a: int, b: int, c: int) -> bool:
    return any(eval(f'{a} {e} {b} == {c}') for e in '+-*/')
