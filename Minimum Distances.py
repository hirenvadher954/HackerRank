import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    counter=0
    sumi=9999999999999999
    if(len(a)==2):
        sumi=1
    else:
     for i in range(0,len(a)-1):
        psum=9999999999999
        for j in range(i+1,len(a)-1):
            if a[i]==a[j]:
                psum=abs(j-i)
                
                if psum<sumi:
                    sumi=psum
                    counter+=1
    
    if(counter==0):
        sumi=-1
    return sumi


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
