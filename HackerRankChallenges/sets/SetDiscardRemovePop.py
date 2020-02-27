#!/bin/python3

__author__ = "Manoj Kumar Arram"

n = input()
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command = input().split()
    cmd = command[0]
    if len(command) > 1:
        args = command[1]
        cmd += "(" + ",".join(args) + ")"
    else:
        cmd += '()'
    eval("s." + cmd)
print(s)
