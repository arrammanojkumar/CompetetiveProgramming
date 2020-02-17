__author__ = "Manoj Kumar Arram"

import re

if __name__ == "__main__":
    v = "aeiou"
    c = "qwrtypsdfghjklzxcvbnm"
    m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags=re.I)
    print('\n'.join(m or ['-1']))
