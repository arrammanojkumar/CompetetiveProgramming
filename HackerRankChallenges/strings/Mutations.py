#!/bin/python3

__author__ = "Manoj Kumar Arram"

s = input()
index, ch = input().split()
s = s[:(int(index))] + ch + s[(int(index) + 1):]
print(s)
