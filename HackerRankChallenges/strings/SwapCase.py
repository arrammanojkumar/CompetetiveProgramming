#!/bin/python3

__author__ = "Manoj Kumar Arram"


def swap_case(s):
    return s.swapcase()  # Builtin method
    # return "".join([ch.lower() if ch.isupper() else ch.upper() for ch in s]) Own logic


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
