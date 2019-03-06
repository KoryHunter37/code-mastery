# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    n = str(bin(n)).replace("b", "")
    
    max_count = 0
    count = 0
    for digit in n:
        if int(digit):
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0

    print(max(count, max_count))
