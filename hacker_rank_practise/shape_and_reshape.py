import numpy as np

# Task
#
# You are given a space separated list of nine integers. Your task is to convert this list into a
# X
#
# NumPy array.
#
# Input Format
#
# A single line of input containing
#
# space separated integers.
#
# Output Format
#
# Print the
# X NumPy array.
#

'''
Convert the inputs to a numpy array and reshape them
'''

array_1 = np.array([int(num) for num in input().split()])
print(np.reshape(array_1, (3,3)))

