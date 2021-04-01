# given a square matrix, calculate the absolute difference between the sum of the diagonals
# 1 2 3
# 4 5 6
# 9 8 9
# left to right diagonal sum = 1 + 5 + 9 = 15
# right to left diagonal sum = 3 + 5 + 9 = 17
# absolute difference |15 - 17| = 2


def AbsoluteDiagonalDifference(ar):
    n = len(ar)
    first_diag = 0
    second_diag = 0
    for i in range(n):
        first_diag += ar[i][i]
        second_diag += ar[i][n-1-i]
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


