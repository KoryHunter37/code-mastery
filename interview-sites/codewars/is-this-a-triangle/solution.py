# https://www.codewars.com/kata/is-this-a-triangle/train/python

def is_triangle(a, b, c):
    arr = [a, b, c]
    maximum = max(arr)
    arr.remove(maximum)
    
    return sum(arr) > maximum
