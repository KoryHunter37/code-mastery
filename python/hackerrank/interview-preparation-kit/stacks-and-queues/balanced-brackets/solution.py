# https://www.hackerrank.com/challenges/balanced-brackets/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    
    if len(s) <= 1:
        return 'NO'

    record = deque()

    brackets = {'[':']', ']':'[', '(':')', ')':'(', '{':'}', '}':'{'}
    closing = ']})'

    for b in s:
        if len(record) == 0:
            if b in closing:
                return 'NO'
            else:
                record.append(b)

        else:
            last = record[-1]
            if b in closing:
                if b != brackets[last]:
                    return 'NO'
                else:
                    record.pop()
            else:
                record.append(b)

    return 'YES' if len(record) == 0 else 'NO'




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
