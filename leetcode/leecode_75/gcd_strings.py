#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/greatest-common-divisor-of-strings
"""


class Solution:
    def is_divisible(self, source, target, l1, l2):
        i = 0
        while i < l2:
            if not (i + l1 <= l2 and target[i:(i + l1)] and source == target[i:(i + l1)]):
                return ""
            i += l1
        return source

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = []

        if len(str1) < len(str2):
            source, target, l1, l2 = str1, str2, len(str1), len(str2)
            res.append(self.is_divisible(source, target, l1, l2))
        else:
            source, target, l1, l2 = str2, str1, len(str2), len(str1)
            res.append(self.is_divisible(source, target, l1, l2))
        i = 0
        while i < l1:
            res.append(self.is_divisible(source[0:i], source[i: l1], len(source[0:i]), len(source[i: l1])))
            i += 1
        res = [x for x in res if x]
        res = sorted(res, key=lambda x: len(x))
        print(f"res: {res}")
        return res[0] if res else ""


print(Solution().gcdOfStrings("ABABABAB", "ABAB"))  # ABAB
