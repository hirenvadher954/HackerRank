#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    countValue = 0
    c = Counter(ar)
    for key,val in enumerate(c):
        if c[val]>=2:
            countValue += c[val]//2
    return countValue        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
