# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example

# There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

# 0.400000
# 0.400000
# 0.200000
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos, neg, zer = 0, 0, 0
    l = len(arr)
    for i in arr:
        if i > 0:
            pos += 1
        elif i< 0:
            neg += 1
        else:
            zer += 1
    print(round(pos/l, 6))
    print(round(neg/l, 6))
    print(round(zer/l, 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
