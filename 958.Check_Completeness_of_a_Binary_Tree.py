# No. 958 Check Completeness of Binary Tree

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        if root:
            q.append(root)
        level_Count, invalid = 1, 0
        while q:
            sz = len(q)
            if sz != level_Count:
                invalid += 1
                if invalid > 1:
                    return False
            level_Count*=2
            end = False
            while sz:
                node = q.popleft()
                if end and node:
                    return False
                if not node:
                    end = True
                else:
                    q.extend([node.left, node.right])
                sz -= 1
        return True

    def isCompleteTree2(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        if root:
            q.append(root)
        end = False
        while q:
            sz = len(q)
            while sz:
                node = q.popleft()
                if end and node:
                    return False
                if not node:
                    end = True
                else:
                    q.extend([node.left, node.right])
                sz -= 1
        return True
