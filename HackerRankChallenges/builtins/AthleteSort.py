#!/bin/python3

__author__ = "Manoj Kumar Arram"

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    print("\n".join(map(lambda x: " ".join(map(str, x)), sorted(arr, key=lambda x: x[k]))))
