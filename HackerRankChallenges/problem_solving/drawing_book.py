#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://www.hackerrank.com/challenges/drawing-book/
"""
# !/bin/python3


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    p = 4
    n = 5
    return int(min(p / 2, n / 2 - p / 2))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     p = int(input().strip())
#
#     result = pageCount(n, p)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

print(pageCount(1, 2))
