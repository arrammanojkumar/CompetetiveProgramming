#!/bin/python3

__author__ = "Manoj Kumar Arram"

N, X = input().split()
marks = []
for _ in range(int(X)):
    marks.append(map(float, input().split()))

for student in zip(*marks):
    print(sum(student)/len(student))
