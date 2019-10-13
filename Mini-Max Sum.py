#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total=sum(arr)
    l=[]
    for num in arr:
        l.append(total-num)
    
    print(min(l),end=" ")
    print(max(l))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
