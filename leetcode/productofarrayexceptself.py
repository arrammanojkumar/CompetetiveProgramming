#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
 https://leetcode.com/problems/product-of-array-except-self
"""

nums = [1, 2, 3, 4]
# nums = [-1,1,0,-3,3]
n = len(nums)
prefix_product = 1
postfix_product = 1
result = [0] * n
for i in range(n):
    result[i] = prefix_product
    prefix_product *= nums[i]
for i in range(n - 1, -1, -1):
    result[i] *= postfix_product
    postfix_product *= nums[i]
print(result)
