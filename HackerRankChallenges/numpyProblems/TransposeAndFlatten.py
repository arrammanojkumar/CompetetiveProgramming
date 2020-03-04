#!/bin/python3

__author__ = "Manoj Kumar Arram"

import numpy

n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print(array.transpose())
print(array.flatten())
