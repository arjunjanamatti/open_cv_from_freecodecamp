#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hours = s.split(':')[0]
    if 'PM' in s and hours == '12':
        return s[:-2]
    elif 'PM' in s:
        return str(int(hours)+12)+s[2:-2]
    elif 'AM' in s and hours == '12':
        return '0'+str(int(hours)-12) + s[2:-2]
    elif 'AM' in s:
        return s[:-2]


if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result + '\n')

    # f.close()