import numpy as np

if __name__ == "__main__":
    size = int(input())
    matrix = list(
        list(float(_1) for _1 in input().split(' ')) for _ in range(size)
    )
    print(round(np.linalg.det(matrix), 2))
