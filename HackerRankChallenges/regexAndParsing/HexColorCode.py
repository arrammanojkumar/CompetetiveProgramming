__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    for _ in range(int(input())):
        # print(*re.findall("(?<!\n)#(?i:[\\da-f]{3}){1,2}", input(), re.I), sep='\n')
        codes = [j for j in re.findall(r'[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})[\s:;,)]', input().strip(), re.I)]
        for code in codes:
            print(code)
