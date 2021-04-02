#Sam is a professor at the university and likes to round each student's grade according to these rules:
#
# If the difference between the grade and the next multiple of 5 is less than 3, round up to the next multiple of 5
# If the value of grade is less than 38 no rounding occurs as the result will still be a failing grade.


import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        if grade % 5 ==0 | grade < 38:
            result.append(grade)
        elif grade < 38:
            result.append(grade)
        else:
            next_multiple = ((grade//5) + 1) * 5
            if (next_multiple - grade) < 3:
                result.append(next_multiple)
            else:
                result.append(grade)
    return result

def grade_round_students(grades):
    result = []
    for grade in grades:
        if grade >= 38:
            mod5 = grade % 5
            if mod5 >= 3:
                grade += 5-mod5
        result.append(grade)
    return grade


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(*result)
