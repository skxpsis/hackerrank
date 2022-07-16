#       TITLE: Plus Minus
# DESCRIPTION: Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
#              Print the decimal value of each fraction on a new line with  places after the decimal.
#              Note: This challenge introduces precision problems. 
#                    The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
#     EXAMPLE: There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
#              0.400000
#              0.400000
#              0.200000
#
# Algorithm details:
#   Nothing too fancy -- simple loop through each element item and increment the appropriate counter
#   Print results to 6 decimal places (trailing zeroes if needed)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    size = len(arr)                                                          # size of array
    positive = 0.0                                                           # positive counter -- this is float so it will calculate with float type
    negative = 0.0                                                           # negative counter
    zero = 0.0                                                               # zero counter
    
    for num in range(size):                                                  # looping through input
        number = arr[num]                                                    # easy to reference element at the current index
        if number < 0:                                                       # if the number is negative
            negative += 1                                                    #    increment neg counter
        elif number > 0:                                                     # if the number is positive
            positive += 1                                                    #    increment pos counter
        else:                                                                # else number has to be 0
            zero += 1                                                        #    so increment zero counter
            
    positive_ratio = format(positive/size, '.6f')                            # calculate positive ratio & add precision to 6 decimal points
    negative_ratio = format(negative/size, '.6f')                            # calculate negative ratio & add precision to 6 decimal points
    zero_ratio = format(zero/size, '.6f')                                    # calculate zero ratio & add precision to 6 decimal points
    
    print(positive_ratio, '\n', negative_ratio, '\n', zero_ratio, sep='')    # format output with each ratio on a newline, sep='' to remove spacing between vars
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
