# https://www.codewars.com/kata/sum-of-two-lowest-positive-integers/train/python

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])