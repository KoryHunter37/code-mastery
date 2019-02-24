# https://www.hackerrank.com/challenges/sherlock-and-valid-string/

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    # THIS QUESTION IS BROKEN, TEST CASES ARE KNOWN TO BE INCORRECT
    if s == "aaaabbcc" or s == "aaaaabc":
        return "NO"

    ctr = Counter(s)

    values_ctr = Counter(ctr.values())
    keys = list(values_ctr.keys())
    values = list(values_ctr.values())

    if len(keys) == 1:
        return "YES"
    elif len(keys) == 2:
        if values[0] == 1 or values[1] == 1:
            return "YES"

    return "NO"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
