#!/bin/python3

import math
import os
import random


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    addition = sum(bill)/2
    if addition == b:
        print("Bon Appetit")
    else:
        print(int(b-addition))    



if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
