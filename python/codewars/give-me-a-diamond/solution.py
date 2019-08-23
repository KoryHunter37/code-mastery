# https://www.codewars.com/kata/give-me-a-diamond/train/python

def diamond(n):

    # Return None if the input is an even number or negative, as it is not possible
    # to print a diamond of even or negative size.
    if n %2 == 0 or n < 0:
        return None

    result = []
    for i in range(n):
        stars = n - 2 * abs(i - n//2)
        spaces = (n - stars) // 2
        result.append(' ' * spaces + '*' * stars)
        
    return '\n'.join(result) + '\n'
 