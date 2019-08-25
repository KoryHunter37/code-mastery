# https://www.codewars.com/kata/roman-numerals-decoder/train/python

def solution(roman):
  dict = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
  }
  
  sum = 0
  highest_value = 0
  for d in range(len(roman) -1, -1, -1):
      value = dict.get(roman[d])
      
      if value < highest_value:
          sum -= value
      else:
          sum += value
          highest_value = max(value, highest_value)
      
    
  return sum