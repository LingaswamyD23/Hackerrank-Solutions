#!/bin/python3

import sys

def fibo(N):
    even_sum = 0
    n1, n2 = 0, 1
    while n2 < N:
        if n2%2 == 0:
            even_sum += n2
        n1, n2 = n2, n1+n2
    return even_sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fibo(n))
