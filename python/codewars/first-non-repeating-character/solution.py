# https://www.codewars.com/kata/first-non-repeating-character/train/python

def first_non_repeating_letter(string):

    for char in string:
        occurences = string.count(char)
        if char.swapcase() != char:
            occurences += string.count(char.swapcase())
        if occurences == 1:
            return char
    
    return ''