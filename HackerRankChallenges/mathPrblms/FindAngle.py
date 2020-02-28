#!/bin/python3

__author__ = "Manoj Kumar Arram"

import math

AB = int(input())
BC = int(input())
print(str(int(round(math.degrees(math.atan2(AB, BC))))) + '°')
