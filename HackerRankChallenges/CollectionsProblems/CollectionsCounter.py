#!/bin/python3

__author__ = "Manoj Kumar Arram"

from collections import Counter

X = int(input())
shoes = Counter(list(map(int, input().split())))
total = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if size in shoes and shoes[size] > 0:
        total += price
        shoes[size] -= 1
print(total)
