#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(a, b, c, d):
    if a - c == 0:
        return ("YES")

    if d - b == 0:
        return ("NO")

    if ((a - c) % (d - b) == 0 and (a - c) // (d - b) >= 0):
        return ("YES")
    return ("NO")

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)