#!/bin/python3

__author__ = "Manoj Kumar Arram"

import numpy

nums = tuple(map(int, input().split()))
print(numpy.zeros(nums, dtype=numpy.int))
print(numpy.ones(nums, dtype=numpy.int))
