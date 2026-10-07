# No. 235 LCA of BST
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cur = root
        mn, mx = p.val, q.val
        if mn > mx:
            mn, mx = mx, mn

        while cur:
            if mn > cur.val:
                cur = cur.right
            elif mx < cur.val:
                cur = cur.left
            else:
                return cur

        return cur
