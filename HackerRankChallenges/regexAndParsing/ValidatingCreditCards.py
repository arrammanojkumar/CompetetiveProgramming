__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    n = int(input())
    valid_structure = r"[456]\d{3}(-?\d{4}){3}$"
    no_four_repeats = r"((\d)-?(?!(-?\2){3})){16}"
    filters = valid_structure, no_four_repeats

    for _ in range(n):
        cc = input()
        if all(re.match(f, cc) for f in filters):
            print("Valid")
        else:
            print("Invalid")
