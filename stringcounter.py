#!/bin/python3

__author__ = "Manoj Kumar Arram"
# Write a program to convert the string from aaabbbccdda to 3a3b2c2d1a

input_ = "aaabcbbccdda"
input_ = list(input_)

c = 1
for each in range(len(input_)):
    current = input_[each]
    if each+1 < len(input_):
        if current == input_[each+1]:
            c += 1
        else:
            print(c, current)
            c = 1
    else:
        print(c, current)
