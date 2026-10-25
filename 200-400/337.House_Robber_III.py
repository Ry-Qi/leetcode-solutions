# No. 337 Rob 3
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
# Besides the root, each house has one and only one parent house.
# After a tour, the smart thief realized that all houses in this place form a binary tree.
# It will automatically contact the police if two directly-linked houses were broken into on the same night.
# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

class Solution:
    def rob(self, root: TreeNode | None) -> int:

        cache = {}
        def dfs(root, valid):
            if not root:
                return 0
            if (root, valid) in cache:
                return cache[(root, valid)]
            res = 0
            if valid:
                res = root.val + dfs(root.left, False) + dfs(root.right, False)
                res = max(res, dfs(root.left, True) + dfs(root.right, True))
            else:
                res = dfs(root.left, True) + dfs(root.right, True)
            cache[(root, valid)] = res
            return res

        return dfs(root, True)
