#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    print(n)
    rows = [0]*n
    columns = [0]*n
    for i in range(n):
        for j in range(n):
            rows[i] += container[i][j]
            columns[i] += container[j][i]

    if sorted(rows) == sorted(columns):
        return 'Possible'
    else:
        return 'Impossible'
    pass

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result + '\n')

    # fptr.close()
