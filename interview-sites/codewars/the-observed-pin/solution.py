# https://www.codewars.com/kata/the-observed-pin/train/python

import itertools

def get_pins(observed):
  '''TODO: This is your job, detective!'''
  
  keypad = {
  '1': ['1', '2', '4'],
  '2': ['1', '2', '3', '5'],
  '3': ['2', '3', '6'],
  '4': ['1', '4', '5', '7'],
  '5': ['2', '4', '5', '6', '8'],
  '6': ['3', '5', '6', '9'],
  '7': ['4', '7', '8'],
  '8': ['0', '5', '7', '8', '9'],
  '9': ['6', '8', '9'],
  '0': ['0', '8']
  }
  
  code = [keypad[digit] for digit in observed]
  code = list(itertools.product(*code))
  code = [''.join(e) for e in code]
  return code
  