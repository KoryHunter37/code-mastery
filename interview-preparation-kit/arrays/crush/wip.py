# https://www.hackerrank.com/challenges/crush/

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    sum_arr = [0] * n

    for query in queries:
        print(query)
        min_index, max_index, add = query[0] - 1, query[1] - 1, query[2]

        # Prefix Sum
        sum_arr[min_index] += add

        if max_index + 1 < len(sum_arr):
            sum_arr[max_index + 1] -= add
    
    for i in range(len(sum_arr)):
        if i == 0:
            arr[i] = sum_arr[i]
        else:
            arr[i] = arr[i-1] + sum_arr[i]

    return max(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
