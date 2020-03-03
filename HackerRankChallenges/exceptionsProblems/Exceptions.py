#!/bin/python3

__author__ = "Manoj Kumar Arram"

for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ValueError as ve:
        print("Error Code: ", ve)
    except ZeroDivisionError as zde:
        print("Error Code: ", zde)
