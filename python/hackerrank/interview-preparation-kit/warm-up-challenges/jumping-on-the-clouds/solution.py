# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    clouds = list(c)
    
    path = 0
    i = 0
    while i < len(clouds) - 1:
        print(i)
        if i + 1 < len(clouds):
            cloud1 = clouds[i+1]
        else:
            cloud1 = 1
            
        if i + 2 < len(clouds):
            cloud2 = clouds[i+2]
        else:
            cloud2 = 1
            
        if cloud2 == 0:
            path += 1
            i += 2
        elif cloud1 == 0:
            path += 1
            i += 1
    
    return path
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
