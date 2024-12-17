#!/bin/python3

__author__ = "Manoj Kumar Arram"

from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    i = input()
    d[i] = d.get(i, 0) + 1
print(len(d.items()))
print(*d.values())
