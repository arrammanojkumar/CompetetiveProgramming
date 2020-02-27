#!/bin/python3

__author__ = "Manoj Kumar Arram"

n = input()
s = set(map(int, input().split()))
b = input()
bs = set(map(int, input().split()))
print(len(set(s.intersection(bs))))
