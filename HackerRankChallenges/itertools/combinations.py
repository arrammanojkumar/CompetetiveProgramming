__author__ = "Manoj Kumar Arram"

from itertools import combinations

if __name__ == "__main__":
    s, K = input().split(" ")
    print(*[''.join(i) for k in range(1, int(K)+1) for i in combinations(sorted(s), k)], sep='\n')
