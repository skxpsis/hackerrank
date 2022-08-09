# TTILE: Tower Breakers

# Notes:
# It's a trick. So for the case with 6, we have the options 3, 5. Why? Because 6-3=3; 6/3 = 2 with 0 remainder. 6-5=1; 6/1 = 6 with 0 remainder. 
# So the trick is that what you remove should leave the tower with enough so that the initial value divides exactly by it (no remainder!).
# Then, at the end, they throw it all out the window and say "the players always choose optimally. 
# "Optimally" means that you always try to "destroy" the tower, meaning you leave it with 1.
# So basically every player always reduces a tower down to 1 and hopes he wins. See above comments for a more elaborate explanation.

# Even though I got the answer and the underlying logic, I still think this is actually a very tough problem. I say so because of the following reasons:
# You have to first understand the complicated game and its rules properly (slightly challenging)
# You then have to find the correct way to win this game from the perspective of each player (extremely challenging)
# So basically, there are two cases here. 
# Both cases rely heavily on the idea that an even number of towers (say 2n) can be thought of as a collection of n pairs of towers.
# CASE 1) If there are an even number of towers Player 1 will go first, and Player 2 will basically copy player 1. 
# Whatever player 1 does to a tower, player 2 will do the exact same thing to the other tower belonging to the same pair. In this case Player 2 will always win.
# CASE 2) If there are an odd number of towers Player 1 will go first, and simply destroy any single tower by setting it equal to 1. 
# Now we again have the same situation from CASE 1 but this time the roles of both players have been reversed. In this case Player 1 will always win.
# Finally, there is also the trivial case where n does not matter because m = 1. In this case Player 2 will obviously always win.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    if m == 1:
        return 2
    elif n % 2 == 0:
        return 2
    else:
        return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
