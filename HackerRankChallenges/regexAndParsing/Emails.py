__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    for _ in range(int(input())):
        name, email = input().split(" ")
        m = re.match(r"[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>", email)
        if m:
            print(name, email)
