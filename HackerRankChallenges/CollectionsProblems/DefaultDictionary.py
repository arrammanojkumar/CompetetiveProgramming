#!/bin/python3

__author__ = "Manoj Kumar Arram"

from collections import defaultdict

m, n = input().split()
A = defaultdict(list)

for _ in range(int(m)):
    A[input()].append(_+1)

for _ in range(int(n)):
    i = input()
    if len(A[i]) > 0:
        print(*A[i])
    else:
        print(-1)
