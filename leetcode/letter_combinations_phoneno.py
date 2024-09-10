#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

map = {1: "",
       2: "abc",
       3: "def",
       4: "ghi",
       5: "jkl",
       6: "mno",
       7: "pqrs",
       8: "tuv",
       9: "wxyz",
       0: ""}

digits = "234"
ans = [""]
for i in digits:
    s = map[int(i)]
    ss = []
    for a in ans:
        for b in s:
            ss.append(a+b)
    ans = ss
    # ans = [a + b for a in ans for b in s]
print(ans)
