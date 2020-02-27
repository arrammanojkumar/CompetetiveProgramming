#!/bin/python3

__author__ = "Manoj Kumar Arram"

k = int(input())
a = list(map(int, input().split()))
s = set(a)
print(((sum(s) * k) - sum(a)) // (k - 1))
