#!/bin/python3

__author__ = "Manoj Kumar Arram"

from typing import List

"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
# https://leetcode.com/problems/two-sum
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def get_index_of(n, lists, offset=0):
            if n in lists[offset:]:
                return offset + lists[offset:].index(n)
            return -1

        for each in range(len(nums)):
            idx = get_index_of((target - nums[each]), nums, each + 1)
            if idx != -1:
                return [each, idx]
