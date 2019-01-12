# https://www.hackerrank.com/challenges/new-year-chaos/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps = 0

    for i in range(0, len(q)):
        if i <= q[i] - 4:
            print("Too chaotic")
            return

    while True:
        #print(q)
        error = False
        for i in range(1, len(q)):
            if q[i] < q[i-1]:
                q[i], q[i-1] = q[i-1], q[i]
                swaps += 1
                error = True
            elif i == len(q)-1 and not error:
                print(swaps)
                return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

