https://www.hackerrank.com/challenges/minimum-swaps-2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    
    while sorted(arr) != arr:
        # Double Swap
        for i in range(0, len(arr)):
            if sorted(arr) == arr:
                break
            for j in range(0, len(arr)):
                if i != j:
                    if arr[i] == j and arr[j] == i:
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps += 1           
                    
        if sorted(arr) == arr:
            break
                    
        # Single Swap
        for i in range(0, len(arr)):
            if sorted(arr) == arr:
                break
            for j in range(0, len(arr)):
                if i != j:
                    if arr[i] == j or arr[j] == i:
                        arr[i], arr[j] = arr[j], arr[i]
                        swaps += 1
                        
    return swaps
                    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
