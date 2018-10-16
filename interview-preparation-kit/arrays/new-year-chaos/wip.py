# https://www.hackerrank.com/challenges/new-year-chaos/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    total_count = 0
    too_chaotic = False

    if not too_chaotic:
        for i in range(0, len(q)):
            count = 0
            for p in range(i+1, len(q)):
                if q[i] > q[p]:
                    count += 1
                    if count > 2 and not too_chaotic:
                        print("Too chaotic")
                        too_chaotic = True
                        break
            if too_chaotic:
                break
            else:
                total_count += count
                
        if not too_chaotic:
            print(total_count)
            
            
                
            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
