#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    cum_list = 0
    day = 1
    first = 5
    like = first // 2
    cum_list += like
    while day < n:
        shared = like*3
        like = shared//2
        cum_list += like
        day += 1

    return cum_list
    pass

if __name__ == '__main__':
    # fptr = open(os.environ['OUT.PUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    print(str(result) + '\n')

    # fptr.close()
