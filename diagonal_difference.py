# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# in progress - code comments

#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # calculate left diagonal
    # calculate right diagonal
    left_diagonal = 0
    right_diagonal = 0
    size = len(arr)
    n = size-1
    
    for i in range(size):
        right_diagonal += arr[i][i]
        left_diagonal += arr[i][n]
        n -= 1
    diagonal_sum = abs(right_diagonal-left_diagonal)
    return diagonal_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
