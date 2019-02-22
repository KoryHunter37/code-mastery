# https://www.hackerrank.com/challenges/ctci-bubble-sort/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    error_found = True
    swaps = 0

    while error_found:
        error_found = False     

        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps += 1
                error_found = True

    print('Array is sorted in {num_swaps} swaps.'.format(num_swaps=swaps))
    print('First Element: {first_element}'.format(first_element=a[0]))
    print('Last Element: {last_element}'.format(last_element=a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
