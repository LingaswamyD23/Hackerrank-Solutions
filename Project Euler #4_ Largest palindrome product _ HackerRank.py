#!/bin/python3

import sys

    
t = int(input().strip())
lst = set(a*b for a in range(999, 99, -1) for b in range(a, 99, -1) if str(a*b) == str(a*b)[::-1])
for _ in range(t):
    n = int(input().strip())
    print(max(i for i in lst if i < n))
