#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/merge-strings-alternately
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        rem = word1[len(word2):len(word1)] if len(word1) > len(word2) else word2[len(word1):len(word2)]
        for i, j in zip(list(word1), list(word2)):
            result += i + j
        result += rem

        return result


print(Solution().mergeAlternately("abc", "defghij"))
