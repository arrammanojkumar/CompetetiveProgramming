#!/bin/python3

__author__ = "Manoj Kumar Arram"


cube = lambda x: pow(x, 3)  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    prev = 0
    cur = 1

    fibs = list()
    fibs.append(prev)
    fibs.append(cur)

    for _ in range(2, n):
        fib = prev + cur
        prev, cur = cur, fib
        fibs.append(fib)
    return fibs[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
