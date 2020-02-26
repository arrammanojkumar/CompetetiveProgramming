#!/bin/python3

__author__ = "Manoj Kumar Arram"
s = input()
print(any(_.isalnum() for _ in s))
print(any(_.isalpha() for _ in s))
print(any(_.isdigit() for _ in s))
print(any(_.islower() for _ in s))
print(any(_.isupper() for _ in s))
