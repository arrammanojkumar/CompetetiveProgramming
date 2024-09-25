#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/move-zeroes/description/
"""

nums = [1, 0, 1, 0, 3, 12]
nums = [0, 1, 1, 1, 1, -1, 0]

left = 0

for right in range(len(nums)):
    if nums[right] != 0:
        nums[right], nums[left] = nums[left], nums[right]
        left += 1

print(nums)
