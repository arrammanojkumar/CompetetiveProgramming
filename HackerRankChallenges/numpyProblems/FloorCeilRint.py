#!/bin/python3

__author__ = "Manoj Kumar Arram"

import numpy

A = numpy.array(input().split(), float)

numpy.set_printoptions(sign=' ')
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
