#!/bin/python3

import math
import os
import random
import re
import sys
import string
# https://www.hackerrank.com/challenges/ctci-making-anagrams/

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    d_a = dict.fromkeys(string.ascii_lowercase, 0)
    d_b = dict.fromkeys(string.ascii_lowercase, 0)

    for letter in a:
        d_a[letter] += 1

    for letter in b:
        d_b[letter] += 1

    deletions = sum([abs(d_a[letter] - d_b[letter]) for letter in string.ascii_lowercase])

    return deletions
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
