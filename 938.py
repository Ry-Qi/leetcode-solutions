# No. 938 Range Sum Of Binary Tree

# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:

        if not root:
            return 0
        res = 0
        if low <= root.val <= high:
            res += root.val
            res += self.rangeSumBST(root.left, low, high)
            res += self.rangeSumBST(root.right, low, high)

        if root.val > high:
            res += self.rangeSumBST(root.left, low, high)
        if root.val < low:
            res += self.rangeSumBST(root.right, low, high)

        return res
