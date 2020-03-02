#!/bin/python3

__author__ = "Manoj Kumar Arram"

from collections import namedtuple

N = int(input())
student = namedtuple('student', input().strip().split())
print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N)) / N)
