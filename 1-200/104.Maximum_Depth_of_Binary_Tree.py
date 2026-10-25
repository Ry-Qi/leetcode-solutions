# No. 104 MaxDepth Of Binary Tree
# 给定一个二叉树 root，返回其最大深度。

# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return 1 + max(l, r)
