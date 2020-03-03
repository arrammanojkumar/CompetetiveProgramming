#!/bin/python3

__author__ = "Manoj Kumar Arram"

from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    # This can be solved with rpartition
    # item, space, qty = input().rpartition(' ')
    details = input().split()
    item = " ".join(details[:-1])
    price = details[-1]
    d[item] = d.get(item, 0) + int(price)
for item, qty in d.items():
    print(item, qty)
