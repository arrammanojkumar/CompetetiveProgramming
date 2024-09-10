#!/bin/python3

__author__ = "Manoj Kumar Arram"

from collections import defaultdict

"""
https://leetcode.com/problems/group-anagrams/description/
"""

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_map = defaultdict(list)

for word in strs:
    sorted_word = ''.join(sorted(word))
    anagram_map[sorted_word].append(word)

print(list(anagram_map.values()))
