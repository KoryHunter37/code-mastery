# https://www.codewars.com/kata/gap-in-primes/train/python

from collections import deque
from math import sqrt, ceil

def is_prime(candidate):
    if candidate > 2 and candidate % 2 == 0:
        return False
            
    for i in range(2, ceil(sqrt(candidate)) + 1):
        if candidate % i == 0:
            return False
            
    return True


def gap(g, m, n):
    primes = deque([float('-inf'), float('-inf')], 2)
    
    for i in range(m, n+1):
    
        if is_prime(i):
            print(i)
            primes.append(i)
            if abs(primes[0] - primes[1]) == g:
                return list(primes)
                
    return None