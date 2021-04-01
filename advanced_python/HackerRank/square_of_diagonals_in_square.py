# given a square matrix, calculate the absolute difference between the sum of the diagonals
# 1 2 3
# 4 5 6
# 9 8 9
# left to right diagonal sum = 1 + 5 + 9 = 15
# right to left diagonal sum = 3 + 5 + 9 = 17
# absolute difference |15 - 17| = 2


def AbsoluteDiagonalDifference(ar):
    n_rows = len(ar)
    n_cols = len(ar)
    first_diag = 0
    second_diag = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if (row == col) & (row != len(ar)//2  and col != len(ar)//2):
                first_diag += ar[row][col]
            elif (row == (len(ar)-1) and col == 0) | (row == 0 and col == (len(ar)-1)):
                second_diag += ar[row][col]
    middle_value = ar[len(ar)//2][len(ar)//2]
    first_diag = first_diag + middle_value
    second_diag = second_diag + middle_value
    return abs(first_diag - second_diag)


# https://www.youtube.com/watch?v=Ou04R30aHq8&list=PL_8jNcohs27XQfEmWAHCgLFqpsNaWxUSe&index=6



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # ar_count = int(input())
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = AbsoluteDiagonalDifference(arr)
    print(str(result) + '\n')


