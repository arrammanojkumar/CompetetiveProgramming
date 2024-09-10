#!/bin/python3

__author__ = "Manoj Kumar Arram"
"""
Given a string s, return the longest palindromic substring in s.

https://leetcode.com/problems/longest-palindromic-substring/description/
"""


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
def is_palindrome(string):
    mid = len(string)/2
    last = len(string)-1
    start = 0
    while last >= mid or start <= mid:
        if not string[last] == string[start]:
            return False
        last -= 1
        start += 1
    return True


def substrings(s):
    for length in range(len(s), 0, -1):
        for start in range(len(s) - length + 1):
            string = s[start: start + length]
            if is_palindrome(string):
                return string


print(substrings("abb"))
