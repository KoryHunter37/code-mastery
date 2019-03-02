# https://www.hackerrank.com/challenges/30-review-loop/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    strings = []
    for i in range(n):
        strings.append(str(input()))

    for string in strings:
        left, right = [], []
        for i in range(len(string)):
            if i % 2 == 0:
                left.append(string[i])
            else:
                right.append(string[i])

        print("".join(left) + " " + "".join(right))
