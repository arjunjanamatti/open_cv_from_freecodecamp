# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with places after the decimal.

# Complete the plusMinus function below.
def plusMinus(arr):
    pos_num = 0
    neg_num = 0
    zero_num = 0
    for i in arr:
        if i > 0:
            pos_num += 1
        elif i < 0:
            neg_num += 1
        else:
            zero_num += 1
    print(pos_num/len(arr))
    print(neg_num/len(arr))
    print(zero_num/len(arr))

    return pos_num/len(arr), neg_num/len(arr), zero_num/len(arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)