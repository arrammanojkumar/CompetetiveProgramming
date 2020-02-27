#!/bin/python3

__author__ = "Manoj Kumar Arram"

input()
s = set(map(int, input().split(' ')))
print(sum(s) / len(s))
