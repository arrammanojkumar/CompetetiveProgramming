#!/bin/python3

__author__ = "Manoj Kumar Arram"

import copy

"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst
"""


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []
        if root == None:
            return False
        stack = []
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                if k-root.val in l:
                    return True
                l.append(root.val)
                root = root.right
            else:
                break
        return False
