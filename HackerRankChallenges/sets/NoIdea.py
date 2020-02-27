#!/bin/python3

__author__ = "Manoj Kumar Arram"

n, m = input().split()
array = list(map(int, input().split()))
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
print(sum([(i in a) - (i in b) for i in array]))
