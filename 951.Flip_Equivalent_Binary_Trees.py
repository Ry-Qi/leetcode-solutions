# No. 951 Flip Equivalent Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flipEquiv(self, root1, root2) -> bool:

        def dfs1(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return (dfs1(root1.left, root2.left) and dfs1(root1.right, root2.right)
                  or dfs1(root1.left, root2.right) and dfs1(root1.right, root2.left))

        return dfs1(root1, root2)
