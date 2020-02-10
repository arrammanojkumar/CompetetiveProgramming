from itertools import product

if __name__ == "__main__":
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    print(*list(product(l1, l2)))

