import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_score = max_score = scores[0]
    min_count = max_count = 0
    for score in scores[1:]:
        if score < min_score:
            min_score = score
            min_count +=1
        if score>max_score:
            max_score = score
            max_count +=1
    return [max_count, min_count]
    