# The included code stub will read an integer,
#
# , from STDIN.
#
# Without using any string methods, try to print the following:
#
# Note that "
#
# " represents the consecutive values in between.
#
# Example
# Print the string
#
# .
#
# Input Format
#
# The first line contains an integer
#
# .
#
# Constraints
#

def PrintNumbers(number):
    for n in range(1, number + 1):
        print(n, end="")

number = int(input('Enter the number: '))
PrintNumbers(number)