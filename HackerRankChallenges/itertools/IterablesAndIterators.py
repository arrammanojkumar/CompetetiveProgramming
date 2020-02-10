from itertools import combinations

length = int(input())
words = input().split()
kCombinations = int(input())

comb = list(combinations(words, kCombinations))
aCombinations = filter(lambda c: 'a' in c, comb)
print("{0:.3}".format(len(list(aCombinations))/len(comb)))
