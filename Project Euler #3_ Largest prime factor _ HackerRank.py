#!/bin/python3

import sys


import math

def isPrime(n): # Finds whether n is prime or not.
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def largest_prime_factor(n):
    max = 1
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            if isPrime(n//i) and n//i > max:
                max = n//i
                break
            elif isPrime(i): max = i        
    return max


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime_factor(n))
