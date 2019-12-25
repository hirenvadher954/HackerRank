#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    temp = 1
    for i in range(1,n+1):
        temp = temp*i
    print(temp)  

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
