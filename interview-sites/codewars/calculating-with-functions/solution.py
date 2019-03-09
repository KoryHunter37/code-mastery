# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def zero(n=None):
    if n is None:    
        return 0
    return n[0](0, n[1])
def one(n=None):
    if n is None:    
        return 1
    return n[0](1, n[1])
def two(n=None):
    if n is None:    
        return 2
    return n[0](2, n[1]) 
def three(n=None):
    if n is None:    
        return 3
    return n[0](3, n[1])
def four(n=None):
    if n is None:    
        return 4
    return n[0](4, n[1])
def five(n=None):
    if n is None:    
        return 5
    return n[0](5, n[1])
def six(n=None):
    if n is None:    
        return 6
    return n[0](6, n[1])
def seven(n=None):
    if n is None:   
        return 7
    return n[0](7, n[1])
def eight(n=None):
    if n is None:    
        return 8
    return n[0](8, n[1])
def nine(n=None):
    if n is None:    
        return 9
    return n[0](9, n[1])

def plus(n):
    return (lambda n1, n2: n1 + n2, n)
def minus(n):
    return (lambda n1, n2: n1 - n2, n)
def times(n):
    return (lambda n1, n2: n1 * n2, n)
def divided_by(n):
    return (lambda n1, n2: n1 // n2, n)