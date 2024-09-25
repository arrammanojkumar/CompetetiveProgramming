#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/merge-intervals/description/
"""

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged = []
intervals.sort(key=lambda x: x[0])
prev = intervals[0]
for curr in intervals[1:]:
    if curr[0] <= prev[1]:
        prev[1] = max(prev[1], curr[1])
    else:
        merged.append(prev)
        prev = curr
merged.append(prev)

print(merged)
