# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    min_difference = float("inf")

    for i in range(len(arr) - 1):
        item = arr[i]
        other_item = arr[i+1]
        
        absolute_difference = abs(item - other_item)
        if absolute_difference < min_difference:
            min_difference = absolute_difference

    return min_difference


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
