https://www.hackerrank.com/challenges/two-strings/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1: str, s2: str) -> str:
    s1count = Counter()
    s2count = Counter()
    
    for letter in s1:
        s1count[letter] += 1
    for letter in s2:
        s2count[letter] += 1

    for key in s1count.keys():
        if s1count[key] > 0 and s2count[key] > 0:
            return "YES"
    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
