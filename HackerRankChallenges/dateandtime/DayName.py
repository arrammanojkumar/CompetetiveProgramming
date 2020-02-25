#!/bin/python3

__author__ = "Manoj Kumar Arram"

import calendar

m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
