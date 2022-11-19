#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    ncount = 0
    pcount = 0
    zcount = 0
    for i in arr:
        if i>0:
            pcount +=1
        elif i<0:
            ncount +=1
        elif i==0:
            zcount +=1
        else:
            print("invalid number")
    
    print("{:0.6f}".format(pcount/len(arr)))
    print("{:0.6f}".format(ncount/len(arr)))
    print("{:0.6f}".format(zcount/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
