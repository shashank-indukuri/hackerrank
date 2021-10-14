# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example

# The unique element is .
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    # d = {}
    # for i in a:
    #     if i not in d.keys():
    #         d[i] = 1
    #     else:
    #         d[i] = 2
    # for i in d.keys():
    #     if d[i] == 1:
    #         return i
    for i in a:
        if a.count(i) == 1:
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
