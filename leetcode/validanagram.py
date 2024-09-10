#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/valid-anagram/description/
"""

s = "anagram"
t = "nagaram"
# s = 'ab'
# t = 'a'
# s = 'manoj'
# t = 'jonamk'


def is_anagram(s, t):
    s = list(s)
    t = list(t)
    flag = True
    d = dict()

    for each in s:
        if each in d:
            d[each] = d[each] + 1
        else:
            d[each] = 1

    for each in t:
        if each in d:
            d[each] = d[each] - 1
            if d[each] < 1:
                del d[each]
        else:
            flag = False
            break

    if flag != False and len(d.keys()) > 0:
        flag = False

    return flag

