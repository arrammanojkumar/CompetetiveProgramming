#!/bin/python3

__author__ = "Manoj Kumar Arram"

# alphabets = [_ for _ in "abcdefghijklmnopqrstuvwxyz"]
# x = 3
# width = len("-".join(alphabets[0:x]))
#
# for i in range(x, 0, -1):
#     s1 = i - 1
#     e1 = x
#     s2 = s1 + 1
#     print(("-".join(alphabets[s1:e1][::-1]) + "-".join(alphabets[s2:e1])).center(width*2, "-"))

size = 3
myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]

for i in range(size - 1, -size, -1):
    x = abs(i)
    line = myStr[size:x:-1] + myStr[x:size]
    print("--" * x + '-'.join(line) + "--" * x)
