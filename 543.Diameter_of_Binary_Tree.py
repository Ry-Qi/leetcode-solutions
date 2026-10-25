# No. 543 二叉树的直径
# 给你一棵二叉树的根节点，返回该树的 直径。

# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度。这条路径可能经过也可能不经过根节点 root。

# 两节点之间路径的 长度 由它们之间边数表示。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal res
            res = max(res, left+right)

            return 1 + max(left, right)

        dfs(root)

        return res
