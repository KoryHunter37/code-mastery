# https://www.codewars.com/kata/replace-with-alphabet-position/train/python

def alphabet_position(text):
    return " ".join([str(ord(letter)-96) for letter in text.lower() if letter.isalpha()])