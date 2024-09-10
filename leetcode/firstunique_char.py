#!/bin/python3

__author__ = "Manoj Kumar Arram"
"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""

import copy

s = 'leetcode'
s = list(s)
d = dict()
for each in s:
    d[each] = d.get(each, 0) + 1
for idx in range(len(s)):
    if d[s[idx]] == 1:
        print(idx)
        break
