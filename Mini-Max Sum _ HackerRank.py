#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    ls = []
    for i in range(len(arr)):
        if i == 0:
            ls.append(sum(arr[i+1:]))
             
        elif i == len(arr)-1:
            ls.append(sum(arr[:len(arr)-1]))
        else:
            ls.append(sum(arr[:i])+sum(arr[i+1:]))
    print(min(ls), max(ls))
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
