# https://www.codewars.com/kata/simple-pig-latin/train/python

from string import punctuation
from collections import deque

def pig_it(text):
    words = text.split()
    
    result = []
    for word in words:
        if word in punctuation:
            result.append(word)
            
        else:
            new_word = deque(word)
            new_word.rotate(-1)
            result.append(''.join(new_word) + 'ay')
        
    return ' '.join(result)
