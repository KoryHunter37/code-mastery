# https://www.codewars.com/kata/multiples-of-3-or-5/train/python

def solution(number):
    return sum(i for i in range(3, number) if i % 3 == 0 or i % 5 == 0)
  