#!/bin/python3

import sys

n = 10 ** 6
sum_dict = {}
prime = [True for i in range(n + 1)]
prime[0] = prime[1] = False
num = 2
while num * num <= n:
    if prime[num] == True:
        for j in range(num * num, n + 1, num):
            if prime[j]:
                prime[j] = False
    num += 1
psum = 0
for i in range(2, n + 1):
    if prime[i]:
        psum += i
    sum_dict[i] = psum


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_dict[n])