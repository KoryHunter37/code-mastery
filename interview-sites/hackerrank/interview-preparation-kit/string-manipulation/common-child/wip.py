# https://www.hackerrank.com/challenges/common-child/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
import re

# Complete the commonChild function below.
def commonChild(s1, s2):
    ss1 = []
    ss2 = []
    for i in range(1, len(s1) + 1):
        ss1.extend(combinations(s1, r=i))
        ss2.extend(combinations(s2, r=i))

    ss1 = ["".join(s) for s in ss1]
    ss2 = ["".join(s) for s in ss2]

    try:
        return len(sorted( set(ss1) & set(ss2), key=lambda ss: len(ss), reverse=True )[0])
    except:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
