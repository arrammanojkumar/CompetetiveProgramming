#!/bin/python3

__author__ = "Manoj Kumar Arram"

s = input()
sub = input()
c = 0
# Approach 1
for _ in range(len(s)):
    if _ + len(sub) <= len(s) and sub == s[_:_ + len(sub)]:
        c += 1
print(c)

# Approach 2
# import re
#
# match = re.findall('(?=' + sub + ')', s)
# print(len(match))
