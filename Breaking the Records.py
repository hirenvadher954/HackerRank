#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mini = scores[0]
    maxi = scores[0]
    temp1 = temp2 = 0
    for val in scores[1:]:
        if(mini>val):
            print(mini)
            mini = val
            temp1 += 1
        if(maxi<val):
            print(maxi)
            maxi = val
            temp2 +=1
   
    return temp2,temp1 

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
