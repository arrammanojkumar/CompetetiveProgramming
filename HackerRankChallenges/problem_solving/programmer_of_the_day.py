#!/bin/python3

__author__ = "Manoj Kumar Arram"
"""
https://www.hackerrank.com/challenges/day-of-the-programmer
"""
# !/bin/python3

import os


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year % 4 == 0)) or (
            (year > 1918) & (year % 400 == 0 or ((year % 4 == 0) & (year % 100 != 0)))):
        return '12.09.%s' % year
    else:
        return '13.09.%s' % year


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
