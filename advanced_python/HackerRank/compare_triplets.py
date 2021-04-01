# a = [1,2,3] and b = [3,2,1]
# if a[i] > b[i], a is awarded 1 point
# if a[i] < b[i], b is awarded 1 point
# if a[i] == b[i], no points are given
# for above example output will be [1,1]

import os
import sys

def compareTriplets(a,b):
    len_array = len(a)
    alic_list = 0
    bob_list = 0
    for i in range(len_array):
        if a[i] > b[i]:
            alic_list += 1
        elif a[i] < b[i]:
            bob_list += 1
    return alic_list, bob_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # ar_count = int(input())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a,b)
    print(str(result) + '\n')
