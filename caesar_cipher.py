# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. 
# If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
#
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
#
# Sample Input:
# 11
# middle-Outz
# 2
#
# Sample Output
# okffng-Qwvb


######

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphabet = collections.deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    alphabet_shifted = collections.deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    s_list = list(s)
    len_s = len(s_list)
    
    for i in range(k):
        alphabet_shifted.append(alphabet_shifted[i])
        
    for j in range(k):
        alphabet_shifted.popleft()
    
    for i in range(len_s):
        if s_list[i].lower() in alphabet:
            index = alphabet.index(s_list[i].lower())
            if s_list[i].islower():
                s_list[i] = alphabet_shifted[index]
            else:
                s_list[i] = alphabet_shifted[index].upper()
                
    cipher = ''.join(s_list)
    return cipher

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
