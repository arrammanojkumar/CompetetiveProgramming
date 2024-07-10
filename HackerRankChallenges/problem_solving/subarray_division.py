#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://www.hackerrank.com/challenges/the-birthday-bar
"""


# !/bin/python3


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Length should equal to M
    # Sum equal to d
    no_of_ways = 0
    for idx, c in enumerate(s):
        if len(s) >= (idx + m):
            if sum(s[idx: idx + m]) == d:
                no_of_ways += 1

    return no_of_ways


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
