#!/bin/python3

__author__ = "Manoj Kumar Arram"

dot = '.|.'
hiphen = '-'

N, M = map(int, input().split())

pattern = [(dot * (2 * i + 1)).center(M, hiphen) for i in range(N // 2)]
print("\n".join(pattern + ["WELCOME".center(M, hiphen)] + pattern[::-1]))
