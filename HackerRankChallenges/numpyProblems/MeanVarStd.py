#!/bin/python3

__author__ = "Manoj Kumar Arram"

import numpy

N, M = input().split()
A = numpy.array([input().strip().split() for _ in range(int(N))], int)

numpy.set_printoptions(sign=' ')
print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(numpy.std(A, axis=None))
