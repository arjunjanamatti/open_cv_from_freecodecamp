# Example
# candles = [4,4,1,3]
# The maximum height candles are units high. There are 2 of them, so return 2.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    value = max(candles)
    count = 0
    for candle in candles:
        if candle == value:
            count += 1
    return count
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(str(result) + '\n')

    # fptr.close()