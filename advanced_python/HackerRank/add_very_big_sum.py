# calculate and print the sum of the elements in an array, keeping in
# mind some of those integers may be quite large

def addVeryBigSum(ar):
    return sum(ar)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = addVeryBigSum(ar)
    print(str(result) + '\n')
