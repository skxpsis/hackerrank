# code comments in progress :)

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Sample Input: 1 2 3 4 5
# Sample Output: 10 14

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    size = len(arr)
    start = 0
    end = size-1
    min_sum = float("inf")
    max_sum = float("-inf")
    
    for num in range(size):
        if num == 0:
            curr_sum = sum(arr[num+1:end+1])
        elif num == end:
            curr_sum = sum(arr[:end])
        else:
            curr_sum = sum(arr[:num])
            curr_sum += sum(arr[num+1:end+1])
        min_sum = min(min_sum, curr_sum)
        max_sum = max(max_sum, curr_sum)
    print(min_sum, max_sum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
