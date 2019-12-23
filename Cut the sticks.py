#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    l = []
    temp = []
    for val in arr:
        l.append(len(arr))
        if arr:
            mini = min(arr)
            d = arr.count(mini)
            for i in range(d):
                arr.remove(mini)
            for val2 in arr:
                temp.append(val2-mini)
            arr = temp[:]
            temp = []
    m = l.count(0)
    for i in range(m):
        l.remove(0)
    return l   



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
