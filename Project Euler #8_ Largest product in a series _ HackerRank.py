#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = map(int,input().strip().split(' '))
    num = input().strip()
    maxm = 0
    prod = 1
    for x in range((n-k)-1):
        for y in range(0,k):
            prod *= int(num[x+y])
        if prod>maxm:
            maxm = prod
        prod = 1
    
    print(maxm)
