import numpy as np
if __name__ == '__main__':
    coefficients = list(float(_) for _ in raw_input().split(' '))
    x = int(raw_input())
    print np.polyval(coefficients, x)
