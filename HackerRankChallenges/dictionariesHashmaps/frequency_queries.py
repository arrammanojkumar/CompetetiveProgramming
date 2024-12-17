#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://www.hackerrank.com/challenges/frequency-queries/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.

def freqQuery(queries):
    res = []
    print(queries)
    d = dict()
    freq_count = dict()
    for query in queries:
        operation, value = query
        match int(operation):
            case 1:
                if d.get(value, 0) > 0:
                    freq_count[d[value]] -= 1

                d[value] = d.get(value, 0) + 1
                freq_count[d[value]] = freq_count.get(d[value], 0) + 1
            case 2:
                if d[value] > 0:
                    freq_count[d[value]] -= 1
                    d[value] = d.get(value, 1) - 1
                    if d[value] > 0:
                        freq_count[d[value]] += 1
            case 3:
                if freq_count.get(value, 0) > 0:
                    res.append(1)
                else:
                    res.append(0)
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print('\n'.join(map(str, ans)))

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')
    #
    # fptr.close()
