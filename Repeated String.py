#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = s.count('a')
    d = n//len(s)
    count = d*count

    if len(s)*d<n:
        for i in range(n-len(s)*d):
            if s[i]=='a':
                count += 1
    return count                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
