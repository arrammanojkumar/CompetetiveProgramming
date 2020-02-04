from itertools import combinations_with_replacement

if __name__ == "__main__":
    word, kreplacement = input().split(" ")
    for combination in list(tup for tup in list(combinations_with_replacement(sorted(word), int(kreplacement)))):
        print("".join(combination), sep="\n")
