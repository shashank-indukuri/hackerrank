# Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
# Example


# The alphabet is rotated by , matching the mapping above. The encrypted string is .

# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    r = ""
    for c in s:
        if c.isalpha():
        #     byt = bytes(i, "utf-8")
        #     if byt[0] + k > 122 and i.islower():
        #         temp = bytes([(byt[0] + k -122) + 96])
        #     elif byt[0] + k > 90 and i.isupper():
        #         temp = bytes([(byt[0] + k -90) + 64])
        #     else:
        #         temp = bytes([byt[0] + k])
        #     r += temp.decode("utf-8")
        # else:
        #     r += i
            c = (ord(c) + k - 97)%26 + 97 if c.islower() else (ord(c) + k - 65)%26 + 65
            r += chr(c)
        else:
            r += c
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
