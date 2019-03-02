# https://www.codewars.com/kata/disemvowel-trolls/train/python

def disemvowel(string):
    string = ''.join([letter for letter in string if letter.lower() not in "aeiou"])
    return string