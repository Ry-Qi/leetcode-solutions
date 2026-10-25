# No. 110 Balanced Tree

# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(root):
            if not root:
                return 0

            # subTree
            left = dfs(root.left)
            if left==-1:
                return -1
            right = dfs(root.right)
            if right==-1:
                return -1

            # current Tree
            if abs(left-right)>1:
                return -1

            return 1 + max(left, right)

        res = dfs(root)
        if res == -1:
            return False

        return True
