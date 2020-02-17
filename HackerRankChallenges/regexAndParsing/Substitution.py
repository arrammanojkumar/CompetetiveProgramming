__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    for _ in range(int(input())):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))
