#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
"""


# !/bin/python3


#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#


def bonAppetit(bill, k, b):
    # Write your code here
    actual = (sum(bill) - bill[k]) / 2
    if actual == b:
        print("Bon Appetit")
    else:
        print(f"{int(b - actual)}")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
