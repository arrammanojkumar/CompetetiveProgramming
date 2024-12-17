#!/bin/python3

__author__ = "Manoj Kumar Arram"

from collections import Counter

[print(*each) for each in Counter(sorted(input())).most_common(3)]