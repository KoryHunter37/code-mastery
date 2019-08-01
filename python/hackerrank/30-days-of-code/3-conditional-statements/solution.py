# https://www.hackerrank.com/challenges/30-conditional-statements/

#!/bin/python3

import math
import os
import random
import re
import sys

WEIRD = "Weird"
NOT_WEIRD = "Not Weird"


if __name__ == '__main__':
    N = int(input())

    if N % 2 == 1:
        print(WEIRD)
    else:
        if 6 <= N <= 20:
            print(WEIRD)
        elif 2 <= N <= 5 or N > 20:
            print(NOT_WEIRD)
