# https://www.codewars.com/kata/second-variation-on-caesar-cipher/train/python

import string
import math
from itertools import chain

def rotate(letter, shift):
    if letter in string.ascii_lowercase:
        new_letter_value = (ord(letter) + shift - 97) % 26
        return chr(new_letter_value + 97)
    elif letter in string.ascii_uppercase:
        new_letter_value = (ord(letter) + shift - 65) % 26
        return chr(new_letter_value + 65)
    else:
        return letter

def encode_str(strng, shift):        
    prefix = strng[0].lower() + rotate(strng[0].lower(), shift)
    
    m = prefix + "".join([rotate(letter, shift) for letter in strng])    
    size = math.ceil(len(m) / 5)
    
    return [i for i in [ m[0:size], m[size:size*2], m[size*2:size*3], m[size*3:size*4], m[size*4:] ] if i != '']
    

def decode(arr):
    first_letter = arr[0][0]
    second_letter = arr[0][1]
    
    alphabet_twice = string.ascii_lowercase + string.ascii_lowercase
    
    original_index = alphabet_twice.find(first_letter)
    shifted_index = alphabet_twice.find(second_letter, original_index+1)
    shift = shifted_index - original_index
            
    arr = list(chain.from_iterable(arr))
    strng = "".join([rotate(letter, -shift) for letter in arr][2:])
    return strng
    
