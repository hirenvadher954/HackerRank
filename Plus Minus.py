#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus=0
    minus=0
    zero=0
    total = len(arr)
    for value in arr:
        if value>0:
            plus+=1
        elif value<0:
            minus+=1
        else:
            zero+=1       
    print(plus/total)
    print(minus/total) 
    print(zero/total)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
