#!/bin/python3

__author__ = "Manoj Kumar Arram"

consonants = []
vowels = []

# Solution 1 which did not meet time complexity

# def isVowel(c):
#     if c in ['a', 'e', 'i', 'o', 'u']:
#         return True
#     return False
#
#
# def get_all_words(start, isvowel):
#     for ch in range(start, len(s) + 1):
#         if len(s[start:ch]) > 0:
#             if isvowel:
#                 vowels.append(s[start:ch])
#             else:
#                 consonants.append(s[start:ch])
#
#
# def get_count(word):
#     size = len(word)
#     count = 0
#     for i in range(len(s)):
#         if word == s[i:(i + size)]:
#             count += 1
#     return count
#
#
# if __name__ == "__main__":
#     s = input()
#     # s = "BANANA".lower()
#
#     for i in range(len(s)):
#         get_all_words(i, isVowel(s[i]))
#
#     vowels = sum([get_count(vowel) for vowel in list(set(vowels))])
#     consonants = sum([get_count(cons) for cons in list(set(consonants))])
#     if vowels == consonants:
#         print("Draw")
#     elif vowels > consonants:
#         print("Kevin", vowels)
#     else:
#         print("Stuart", consonants)


s = "BANANA"
vowels = "AEIOU"
kevc = 0
stuc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevc += (len(s) - i)
    else:
        stuc += (len(s) - i)
if kevc == stuc:
    print("Draw")
elif kevc > stuc:
    print("Kevin", kevc)
else:
    print("Stuart", stuc)
