#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    m = Counter(arr)
    t = []
    temp = []
    for val in arr:
        if val not in t:
            temp.append(m[val])
            t.append(val)
    temp.remove(max(temp))
    return sum(temp[:])        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
