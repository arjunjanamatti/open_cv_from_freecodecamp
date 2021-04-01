# given an array of integers, find sum of it's elements
# arr = [1,2,3], 1+2+3=6 so return 6

import os
import sys

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    print(str(result) + '\n')
