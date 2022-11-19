#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_of_squares = (n*(n+1)*(2*n+1)) // 6
    sum_of_numbers = (n*(n+1))//2
    total_sum = abs(sum_of_numbers**2 - sum_of_squares)
    print(total_sum)
