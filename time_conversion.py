# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# in progress :) gotta add code comments

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # if end of string == AM, return string
    # elif end of string == PM, do 24 hr conversion
    # by adding 12 + curr time after 12 (so 12+1=13 if its 1pm)
    size = len(s)
    end = size - 1
    suffix = str(s[end-1:end]).lower()
    twelve = str(s[0:2])
    
    if twelve == "12" and suffix == "a":
        hour1 = int(s[:1])
        hour2 = int(s[1:2])
        s_list = list(s)
        s_list[0] = "0"
        s_list[1] = "0"
        s_list.pop(end)
        s_list.pop(end-1)
        s = ''.join(s_list)
    elif twelve == "12" and suffix == "p":
        s_list = list(s)
        s_list.pop(end)
        s_list.pop(end-1)
        s = ''.join(s_list)
    elif twelve != "12" and suffix == "a" :
        s_list = list(s)
        s_list.pop(end)
        s_list.pop(end-1)
        s = ''.join(s_list)
    else:
        hour = int(s[:2])
        total = int(str(hour))
        print(total)
        new_hour = str(12 + total)
        s_list = list(s)
        s_list[0] = new_hour[0]
        s_list[1] = new_hour[1]
        s_list.pop(end)
        s_list.pop(end-1)
        s = ''.join(s_list)

    return(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
