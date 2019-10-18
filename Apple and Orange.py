#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    temp1 = []
    temp2 = []
    count1=count2=0
    for apple in apples:
        temp1.append(apple+a)
    for orange in oranges:
        temp2.append(orange+b)
    for temp in temp1:
        if s<=temp and t>=temp:
            count1 += 1
    for temp in temp2:
        if t>=temp and s<=temp:
            count2 += 1    
    print(count1)
    print(count2)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
