# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example


# Return '12:01:00'.


# Return '00:01:00'
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # if s[:2] == "12" and s[-2:] == "AM":
    #     return "00" + s[2:8]
    # elif s[-2:] == "AM" or (s[:2] == "12" and s[-2:] == "PM"):
    #     return s[:8]
    # else:
    #     return str(str(12 + int(s[:2])) + s[2:8])
    h = int(s[:2])
    msec = s[2:8]
    h = h % 12 if s[-2:] == 'AM' else h % 12 + 12
    return f"{h:02}{msec}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
