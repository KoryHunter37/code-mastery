# https://www.codewars.com/kata/ones-and-zeros/train/python

def binary_array_to_number(arr):
  binary_string = ''.join(str(e) for e in arr)
  return int(binary_string, base=2)
  