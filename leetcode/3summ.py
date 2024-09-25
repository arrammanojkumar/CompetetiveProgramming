#!/bin/python3

__author__ = "Manoj Kumar Arram"

from typing import List

"""
https://leetcode.com/problems/3sum/description/
"""

nums = [-1, 0, 1, 2, -1, -4]
# nums = [12, 13, 12, 13, -3, 3, 11, 7, 10, 5, 1, 6, 6, 14, 2, -8, -1, -4, 3, -10, 3, -13, 7, -15, 12, 10, -2, -14, 3, -3,
#         -7, 0, -12, 12, -1, 0, 0, -13, -8, -12, 7, 0, 9, -1, -8, -12, 6, 6, -1, -13, 3, -13, -11, -4, 9, -14, -9, 14, 9,
#         2, -3, -13, 9, 0, -15, -15, 7, -8, -12, 6, -5, 10, 14, -11, -6, -9, 14, 8, 4, -10, 10, -8, 14, 6, 3, 8, 0, 2, 8,
#         -6, 11, 12, -3, 5, -3, -11, 6, 11, -4, 1, -6, -1, -4, -7, 3, -2, -9, -5, -9, 10, 0, 8, -12, -8, -1]
triplets = []
nums = [-2, 0, 1, 1, 2]


def time_out_solution():
    def seen(lst, element):
        for each in lst:
            if sorted(each) == sorted(element):
                return False
        return True

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    print(nums[i], nums[j], nums[k])
                    if seen(triplets, [nums[i], nums[j], nums[k]]):
                        triplets.append([nums[i], nums[j], nums[k]])


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    ans = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i and nums[i] == nums[i - 1]:
            continue
        j, k = i + 1, n - 1
        while j < k:
            x = nums[i] + nums[j] + nums[k]
            if x < 0:
                j += 1
            elif x > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j, k = j + 1, k - 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return ans


print(threeSum(nums))
