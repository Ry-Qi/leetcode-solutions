# No. 98 Validate Binary Search Tree
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 严格小于 当前节点的数。
# 节点的右子树只包含 严格大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def dfs(root)-> list:
            if not root:
                return [True,float('-inf'), float('inf')]
            ok,left_max,left_min = dfs(root.left)
            if not ok or left_max >= root.val:
                return [False,float('-inf'), float('inf')]
            ok, right_max, right_min = dfs(root.right)
            if not ok or root.val >= right_min:
                return [False,float('-inf'), float('inf')]
            cur_max = max(right_max, left_max, root.val)
            cur_min = min(right_min, left_min, root.val)
            return [True, cur_max, cur_min]

        return dfs(root)[0]
