#!/bin/python3

__author__ = "Manoj Kumar Arram"

from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(Fraction._mul, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
