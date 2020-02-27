#!/bin/python3

__author__ = "Manoj Kumar Arram"

n1 = input()
s1 = set(map(int, input().split()))
n2 = input()
s2 = set(map(int, input().split()))
print('\n'.join(map(str, sorted(s1.symmetric_difference(s2)))))
