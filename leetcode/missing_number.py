#!/bin/python3

__author__ = "Manoj Kumar Arram"
"""
https://leetcode.com/problems/missing-number/
"""
nums = [3,0,1]
n = len(nums)
sum_ = (n * (n + 1)) / 2
print(int(sum_ - sum(nums)))
