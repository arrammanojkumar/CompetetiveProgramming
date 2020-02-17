__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    print(*re.split("[,.]", "100,000,000.000"), sep="\n")
