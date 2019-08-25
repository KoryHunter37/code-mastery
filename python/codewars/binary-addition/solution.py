# https://www.codewars.com/kata/binary-addition/train/python

def add_binary(a,b):
#     This solution would work if Python 3 was supported by this question.
#     binary_to_string = str.maketrans("", "", "b")
#     return str(bin(a+b)).translate(binary_to_string).lstrip("0")
    return str(bin(a+b)).replace("b", "").lstrip("0")