#
# s = [2,2,1,3,2]
# d=4
# m=2
#
# windowStart = 0
# sums = 0
# total = []
# for i in range(len(s)):
#    sums += s[i]
#    if i>=m-1:
#     if sums==d:
#         total.append([s[windowStart], s[i]])
#     sums -=s[windowStart]
#     windowStart+=1
#
# print(total)


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    windowStart = 0
    sums = 0
    count = 0
    for i in range(len(s)):
        sums += s[i]
        if i >= m - 1:
            if sums == d:
                # total.append([s[windowStart], s[i]])
                count += 1
            sums -= s[windowStart]
            windowStart += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
