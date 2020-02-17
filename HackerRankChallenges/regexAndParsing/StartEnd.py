__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    s = input()
    k = input()

    matches = list(re.finditer(r'(?={})'.format(k), s))
    if matches:
        print('\n'.join(str((match.start(),
                             match.start() + len(k) - 1)) for match in matches))
    else:
        print('(-1, -1)')