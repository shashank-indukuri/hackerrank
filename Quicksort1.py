# The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm with a running time of . In these next few challenges, we're covering a divide-and-conquer algorithm called Quicksort (also known as Partition Sort). This challenge is a modified version of the algorithm that only addresses partitioning. It is implemented as follows:

# Step 1: Divide
# Choose some pivot element, , and partition your unsorted array, , into three smaller arrays: , , and , where each element in , each element in , and each element in .

# Example

# In this challenge, the pivot will always be at , so the pivot is .

#  is divided into , , and .
# Putting them all together, you get . There is a flexible checker that allows the elements of  and  to be in any order. For example,  is valid as well.

# Given  and , partition  into , , and  using the Divide instructions above. Return a 1-dimensional array containing each element in  first, followed by each element in , followed by each element in .

# Function Description

# Complete the quickSort function in the editor below.

# quickSort has the following parameter(s):

# int arr[n]:  is the pivot element
# Returns

# int[n]: an array of integers as described above
# Input Format

# The first line contains , the size of .
# The second line contains  space-separated integers  (the unsorted array). The first integer, , is the pivot element, .

# Constraints

#  where 
# All elements are distinct.
# Sample Input

# STDIN       Function
# -----       --------
# 5           arr[] size n =5
# 4 5 3 7 2   arr =[4, 5, 3, 7, 2]
# Sample Output

# 3 2 4 5 7
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def partition(arr, p):
    n = len(arr) - 1
    arr[n], arr[p] = arr[p], arr[n]
    l = -1
    for i in range(n):
        if arr[i] < arr[n]:
            l += 1
            arr[l], arr[i] = arr[i], arr[l]
    arr[n], arr[l+1] = arr[l+1], arr[n]
    return arr
    
def quickSort(arr):
    # Write your code here
    p = 0
    r = partition(arr, p)
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
