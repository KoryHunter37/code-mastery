# https://www.codewars.com/kata/disemvowel-trolls/train/python

def disemvowel(string):
    translation_table = str.maketrans("", "", "aeiouAEIOU")
    return string.translate(translation_table)