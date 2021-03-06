#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    temp = n
    count = 0
    while(n!=0):
        bc = n%10
        if bc!=0 and temp%bc==0:
            count += 1
        n = n//10
    return count         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())


    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
