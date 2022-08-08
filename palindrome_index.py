# Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. 
# There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. 
# Otherwise, return the index of a character to remove.

# Solve this by simultaneously checking both ends, like a normal palindorme problem.
# When there's an inequality, remove each mismatch element at a time and check if the resulting string is a palindrome. 
# Return the index of the element to remove if a palindrome occurs. If neither are, return -1.

########

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isPalindrome(s):
    len_s = len(s)
    for i in range(len_s):
        end = len_s-1-i
        if s[i] != s[end]:
            return False
    return True

def palindromeIndex(s):
    len_s = len(s)
    half_s = len(s)//2
    return_value = -1
    palindrome_check = isPalindrome(s)
    
    if len_s <= 1:
        return return_value
    if palindrome_check == True:
        return return_value
    
    for i in range(half_s):
        end = len_s-1-i
        if s[i] != s[end]:
            s_temp = list(s)
            s_temp.pop(i)
            s_temp = ''.join(s_temp)
            palindrome_check = isPalindrome(s_temp)
            if palindrome_check == True:
                return i
            else:
                s_temp = list(s)
                s_temp.pop(end)
                s_temp = ''.join(s_temp)
                palindrome_check = isPalindrome(s_temp)
                if palindrome_check == True:
                    return end
    return return_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
