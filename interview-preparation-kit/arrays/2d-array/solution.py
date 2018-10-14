# https://www.hackerrank.com/challenges/2d-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses = []
    for y in range(1, len(arr)-1):
        for x in range(1, len(arr[0])-1):
            h = 0
            h += arr[y-1][x-1]
            h += arr[y-1][x]
            h += arr[y-1][x+1]
            h += arr[y+1][x-1]
            h += arr[y+1][x]
            h += arr[y+1][x+1]
            h += arr[y][x]
            hourglasses.append(h)
    
    return max(hourglasses)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
