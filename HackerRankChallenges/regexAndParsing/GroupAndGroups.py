__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    m = re.search(r"(\w(?!_))\1+", input().strip())
    print(m.group(1) if m else -1)
