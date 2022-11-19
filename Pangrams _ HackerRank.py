#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase, punctuation
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# def pangrams(s):
#     # Write your code here
#     s = s.lower()
#     count_dict = {alpha: 0 for alpha in ascii_lowercase}
#     for ch in s:
#         if ch not in punctuation and ch != ' ':
#             count_dict[ch] +=1
#     count_alpha = list(count_dict.values())
#     print(count_alpha)
#     if count_alpha.count(0)>0:
#         return "not pangram"
#     else:
#         return "pangram"
def pangrams(s):
    return "pangram" if len(set([c.lower() for c in s if c.isalpha()])) == 26 else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
