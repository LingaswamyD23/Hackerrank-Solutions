#!/bin/python3

import sys

# def gcd(a,b):
#     while b:
#         a,b = b, a%b
#     return a

# def lcm(a,b):
#     return a*b // gcd(a,b)


from math import gcd

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lcm = 1
    for i in range(1, n + 1):
        lcm = lcm * i // gcd(lcm, i)
    print(lcm)

