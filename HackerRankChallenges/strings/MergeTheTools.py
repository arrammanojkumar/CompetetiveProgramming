#!/bin/python3

__author__ = "Manoj Kumar Arram"

import collections

s = input()
k = int(input())
init = 0
prev = 0
for i in range(init, len(s)+1, init+k):
    if len(s[prev:i]) > 0:
        print("".join(collections.OrderedDict.fromkeys(s[prev:i]).keys()))
    prev = i
