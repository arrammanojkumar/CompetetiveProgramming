__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    print(*("YES" if bool(re.match(r"[7|8|9][0-9]{09}$", input())) else "NO" for _ in range(int(input()))), sep="\n")
