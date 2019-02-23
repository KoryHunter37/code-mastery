# https://www.hackerrank.com/challenges/alternating-characters/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    s = list(s)
    count = 0

    curr_ptr = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
    
    return count

    while curr_ptr < len(s) - 1:
        if s[curr_ptr] == s[curr_ptr + 1]:
            count += 1
            curr_ptr += 1
        else:
            curr_ptr += 1

    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
