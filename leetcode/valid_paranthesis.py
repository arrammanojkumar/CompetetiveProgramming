#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/valid-parentheses/description/
"""

s = "()"
stack = list()
flag = True
pairs = {"(": ")",
         "{": "}",
         "[": "]"
         }

for each in s:
    if each in pairs:
        stack.append(each)
    elif len(stack) == 0 or each != pairs[stack.pop()]:
        flag = False
        break
if flag:
    flag = len(stack) == 0
print(flag)
