# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def zero(n=None):
    if n is None:    
        return 0
    return n(0)
def one(n=None):
    if n is None:    
        return 1
    return n(1)
def two(n=None):
    if n is None:    
        return 2
    return n(2) 
def three(n=None):
    if n is None:    
        return 3
    return n(3)
def four(n=None):
    if n is None:    
        return 4
    return n(4)
def five(n=None):
    if n is None:    
        return 5
    return n(5)
def six(n=None):
    if n is None:    
        return 6
    return n(6)
def seven(n=None):
    if n is None:   
        return 7
    return n(7)
def eight(n=None):
    if n is None:    
        return 8
    return n(8)
def nine(n=None):
    if n is None:    
        return 9
    return n(9)

def plus(n2):
    return (lambda n1: n1 + n2)
def minus(n2):
    return (lambda n1: n1 - n2)
def times(n2):
    return (lambda n1: n1 * n2)
def divided_by(n2):
    return (lambda n1: n1 // n2)