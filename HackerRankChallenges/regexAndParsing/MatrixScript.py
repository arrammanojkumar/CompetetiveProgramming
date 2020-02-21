#!/bin/python3

__author__ = "Manoj Kumar Arram"

import re

n, m = map(int, input().split())
matrix, s = [], ""
for _ in range(n):
    matrix.append(input())

for letter in zip(*matrix):
    s += "".join(letter)
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", s))
