#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://leetcode.com/problems/design-hashmap/
"""

class MyHashMap:

    def __init__(self):
        map = [[]]

    def put(self, key: int, value: int) -> None:
        self.map.add[key] = value

    def get(self, key: int) -> int:
        if key in self.map.keys():
            return self.map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        del self.map[key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)