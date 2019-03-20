# https://app.codesignal.com/arcade/intro/level-7/vExYvcGnFsEYSt8nQ

from math import floor

def circleOfNumbers(n, firstNumber):
    return math.floor((firstNumber + n/2) % n)
