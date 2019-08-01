# https://www.codewars.com/kata/playing-with-digits/train/python

def dig_pow(n, p):    
    digits = list(map(int, str(n)))
    
    digit_sum = sum([digits[i] ** (p+i) for i in range(len(digits))])
    
    result = digit_sum / n
    if result.is_integer():
        return result
    
    return -1