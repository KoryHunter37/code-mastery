# https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    depth = 0
    valleys = 0
    steps = list(s)
    in_valley = False
    
    for step in steps:
        if step == "D":
            depth -= 1
        elif step == "U":
            depth += 1
            
        if not in_valley and depth < 0:
            in_valley = True
        
        if in_valley and depth >= 0:
            in_valley = False
            valleys += 1
        
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
