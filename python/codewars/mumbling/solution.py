# https://www.codewars.com/kata/mumbling/train/python

def accum(s):
    result = []
    
    for i in range(len(s)):
        letter = s[i]
        result.append(letter.upper())
        result.append(letter.lower() * i)
        
        if i < len(s) - 1:
            result.append('-')
    
    return ''.join(result)
