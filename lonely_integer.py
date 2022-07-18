# Given an array of integers, where all elements but one occur twice, find the unique element.
# in progress (code comments)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # loop through arr, a[]
    # keep track of counts of nums in counts dict {}
    # return counts dict key that only has value of 1
    
    size = len(a)
    counts = {}
    
    for num in range(size):
        current_num = a[num]
        if current_num not in counts.keys():
            counts[current_num] = 0
        counts[current_num] += 1
    
    lonely = [key for key, value in counts.items() if value == 1]
    lonely_int = lonely[0]
    return int(lonely_int)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
