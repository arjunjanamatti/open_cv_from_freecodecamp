#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result = []
    cut_length = min(arr)
    first_sticks = len(arr)
    result.append(first_sticks)
    revised_arr = [element-cut_length for element in arr
                   if (element-cut_length) > 0]
    if len(revised_arr) > 0:
        result.append(len(revised_arr))
        while len(revised_arr)>0:
            cut_length = min(revised_arr)
            revised_arr = [element - cut_length for element in revised_arr
                           if (element - cut_length) > 0]
            if len(revised_arr) > 0:
                result.append(len(revised_arr))

    return result



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))
    print('\n')

    # fptr.close()
