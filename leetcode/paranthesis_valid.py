#!/bin/python3

__author__ = "Manoj Kumar Arram"
"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
"""

s = "()))(()))))("
s = "((()))(())())"
s=")()"
s = list(s)
stack = []
count = 0
for index in range(len(s)):
    if "(" in s[index]:
        stack.append(s[index])
    elif ")" in s[index]:
        try:
            stack.pop()
        except:
            count += 1

if len(stack) > 0:
    count += len(stack)

print(count)
