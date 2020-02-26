#!/bin/python3

__author__ = "Manoj Kumar Arram"

s = input()
for _ in s.split():
    s = s.replace(_, _.capitalize())
print(s)
