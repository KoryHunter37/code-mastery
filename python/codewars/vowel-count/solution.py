# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def getCount(inputStr):
    num_vowels = 0
    return sum([1 for letter in inputStr.lower() if letter in "aeiou"])
    
    return num_vowels