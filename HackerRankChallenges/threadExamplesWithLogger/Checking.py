#!/bin/python3

__author__ = "Manoj Kumar Arram"


def isPresent(arr, num):
    for n in arr:
        if n == num:
            print("Same")
            break
    else:
        print("Not exists")

a = 0
b = a if a > 0 else 0
print(b)