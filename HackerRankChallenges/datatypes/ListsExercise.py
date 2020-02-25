#!/bin/python3

__author__ = "Manoj Kumar Arram"

l = []

for _ in range(int(input())):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("l." + cmd)
    else:
        print(l)
