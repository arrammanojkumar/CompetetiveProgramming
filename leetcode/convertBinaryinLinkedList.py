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
    ans = 2*ans + each
print(ans)
