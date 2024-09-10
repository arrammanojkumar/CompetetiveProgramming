#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/reverse-string/description/
"""

s = ["m", "a", "n", "o", "j", "k"]

start = 0
last = len(s)-1

while start < last:
    s[start], s[last] = s[last], s[start]
    start += 1
    last -= 1

print(s)
