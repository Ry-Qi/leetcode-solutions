# No. Path sum
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum。
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum。如果存在，返回 true；否则，返回 false。

# 叶子节点 是指没有子节点的节点。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root, curSum):
            nonlocal targetSum
            curSum += root.val
            if not root.left and not root.right:
                return curSum == targetSum

            if root.left and dfs(root.left, curSum):
                return True
            if root.right and dfs(root.right, curSum):
                return True

            return False

        return dfs(root, 0)
