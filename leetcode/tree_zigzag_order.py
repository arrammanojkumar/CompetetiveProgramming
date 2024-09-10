#!/bin/python3

__author__ = "Manoj Kumar Arram"

from collections import deque
from typing import Optional, List

"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""


def levelorder_traversal(root):
    current_ = next_ = list()
    ltr = True
    if root == None:
        return
    current_.append(root)
    vals = []
    while len(current_) > 0:
        temp = current_.pop()
        if temp:
            vals = [temp.val]
            if ltr:
                p = []
                if temp.left:
                    next_.append(temp.left)
                    p.append(temp.left.val)
                if temp.right:
                    next_.append(temp.right)
                    p.append(temp.right.val)
                vals.append(p)
            else:
                p = []
                if temp.right:
                    next_.append(temp.right)
                    p.append(temp.right.val)
                if temp.left:
                    next_.append(temp.left)
                    p.append(temp.left.val)
                vals.append(p)

        if len(current_) == 0:
            current_, next_ = next_, current_
            ltr = not ltr
    print(vals)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque([root])
        ltr = True
        while q:
            t = []
            for _ in range(len(q)):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            t = t if ltr else t[::-1]
            ans.append(t)
            ltr = not ltr
        return ans
