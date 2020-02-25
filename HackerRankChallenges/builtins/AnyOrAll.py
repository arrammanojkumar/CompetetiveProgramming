#!/bin/python3

__author__ = "Manoj Kumar Arram"
size, numbers = input(), input().split()
print(all([int(n) > 0 for n in numbers]) and any([n == n[::-1] for n in numbers]))
