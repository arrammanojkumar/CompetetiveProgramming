#!/bin/python3

__author__ = "Manoj Kumar Arram"
"""
 https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

"""

# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         answer = 0
#         while head:
#             answer = 2*answer + head.val
#             head = head.next
#         return answer

binary = [1,0]
ans = 0
for each in list(binary):
    print(f"Before each: {each}, 2*ans: {2*ans}, ans: {ans}")
    ans = 2*ans + each
    print(f"After each: {each}, ans: {ans}")
print(ans)
