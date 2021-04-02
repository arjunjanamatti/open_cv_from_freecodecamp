# Given 5 positive integers, find minimum and maximum values that can be calculated by summing
# exactly four of the five integers. Then print respective minimum and maximum values as a
# single line of two space-seperated long integers

# array = [1,3,5,7,9], minimum_sum = 1+3+5+7 = 16, maximum_sum = 3+5+7+9 = 24
arr = list(map(int, input().rstrip().split()))

def min_and_max(arr):
    arr = sorted(arr)
    min_sum = sum(arr[:-1])
    max_sum = sum(arr[1:])
    print(min_sum, end=' ')
    print(max_sum)

def minmax(arr):
    sum_arr = 0
    min_num = 99999999999999999999
    max_num = 0
    for i in arr:
        sum_arr += i
        min_num = min(min_num, i)
        max_num = max(max_num, i)
    print(min_num, max_num)
    print(sum_arr - min_num, end=' ')
    print(sum_arr - max_num)
    pass

min_and_max(arr)
minmax(arr)