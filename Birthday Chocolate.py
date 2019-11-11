#!/bin/python3
import os
import math
import sys
import re
import random


# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:m]) == d:
            count += 1
        m += 1
    return count    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
