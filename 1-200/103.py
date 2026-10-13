# No. 103 ZigZag traversal of Binary Tree

# # Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        q = deque()
        if root:
            q.append(root)
        ok = True
        res = []
        while q:
            sz = len(q)
            level = []
            while sz:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sz-=1
                level.append(node.val)

            if not ok:
                level.reverse()
            res.append(level)
            ok = not ok
        return res
