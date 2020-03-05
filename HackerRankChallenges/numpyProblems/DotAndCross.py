#!/bin/python3

__author__ = "Manoj Kumar Arram"

import numpy

N = int(input())

A = numpy.array([input().strip().split() for _ in range(int(N))], int)
B = numpy.array([input().strip().split() for _ in range(int(N))], int)
print(A.dot(B))
