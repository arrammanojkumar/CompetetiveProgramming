__author__ = "Manoj Kumar Arram"

import re

# ref:https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression

if __name__ == "__main__":
    regex_pattern = r"(?<=^)M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?=$)"

    # thousand = 'M{0,3}'
    # hundred = '(C[MD]|D?C{0,3})'
    # ten = '(X[CL]|L?X{0,3})'
    # digit = '(I[VX]|V?I{0,3})'

    print(bool(re.match(regex_pattern, input())))
