#!/bin/python3

import sys
import math


def prime_number(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

primes = [0,2,3]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    try:
        print(primes[n])
    except:
        lngth = len(primes)
        idx = lngth - 1
        num = primes[idx]
        while lngth <= n + 1:
            num += 2
            if prime_number(num):
                primes.append(num)
                lngth += 1
        print(primes[n])

