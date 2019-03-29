# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/yBFfNv5fTqhcacZ7w

from math import sqrt, isclose

def isPower(n):
    for b in range(2, 10):
        print(n ** (1/b))
        if isclose(n ** (1/b), round(n ** (1/b)),  rel_tol=0.0000001):
            return True
        
    return False
