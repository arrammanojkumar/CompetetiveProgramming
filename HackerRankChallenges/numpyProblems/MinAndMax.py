#!/bin/python3

__author__ = "Manoj Kumar Arram"

import numpy

N, M = input().split()

A = numpy.array([input().strip().split() for _ in range(int(N))], int)
print(numpy.max(numpy.min(A, axis=1)))
