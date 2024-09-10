#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/transpose-matrix/description/
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose = []

for col in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[col])
    transpose.append(new_row)
