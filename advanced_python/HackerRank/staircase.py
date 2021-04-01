# Its base and height are both equal to n
#
# . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.
#
# Write a program that prints a staircase of size n

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    list_1 = [_+1 for _ in range(n)]
    list_2 = [len(list_1)-_ for _ in list_1]
    space = ' '
    has = '#'
    for i in range(len(list_1)):
        print(space*list_2[i]+has*list_1[i])
    pass

if __name__ == '__main__':
    n = int(input())

    staircase(n)
