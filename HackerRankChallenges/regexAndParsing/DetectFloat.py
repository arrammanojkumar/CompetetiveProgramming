__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":

    for _ in range(int(input())):
        print(bool(re.match("^[+-]?\d*\.\d+$", input())))
