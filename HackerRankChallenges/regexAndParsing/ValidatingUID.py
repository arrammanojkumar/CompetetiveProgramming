__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        uid = ''.join(input())
        has_2_or_more_upper = bool(re.search(r'[A-Z]{2,}', uid))
        has_3_or_more_digits = bool(re.search(r'\d{3,}', uid))
        has_10_proper_elements = bool(re.search(r'^[a-zA-Z0-9]{10}$', uid))
        no_repeats = not bool(re.search(r'(.).*\1', uid))

        if has_2_or_more_upper and has_3_or_more_digits and has_10_proper_elements and no_repeats:
            print("Valid")
        else:
            print("Invalid")
