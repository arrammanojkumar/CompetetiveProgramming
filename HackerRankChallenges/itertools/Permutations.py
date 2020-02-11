__author__ = "Manoj Kumar Arram"

from itertools import permutations

if __name__ == "__main__":
    s, k = input().split(" ")
    print(*[''.join(a) for a in list(permutations(sorted(s), int(k)))], sep='\n')
