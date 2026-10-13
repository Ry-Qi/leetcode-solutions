# No. 106 Construct Binary Tree From Inorder and Postorder

# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3] (value always unique in each order）
# 输出：[3,9,20,null,null,15,7]

# Definition for a binary tree node.

import enum


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:

        def dfs(inOrder, postOrder):
            if len(inOrder) != len(postOrder):
                return None
            if len(inOrder) == 0 or len(postOrder) == 0:
                return None
            root_Val = postOrder[-1]
            root = TreeNode(root_Val)
            root_Index_Inorder = -1
            for i, n in enumerate(inOrder):
                if n == root_Val:
                    root_Index_Inorder = i
                    break
            if root_Index_Inorder == -1:
                return None

            left_size = root_Index_Inorder
            left = dfs(inOrder[:root_Index_Inorder], postOrder[:left_size])
            right = dfs(inOrder[root_Index_Inorder+1:], postOrder[left_size:len(postOrder)-1])
            root.left = left
            root.right = right
            return root

        return dfs(inorder, postorder)

    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:

        pos_map = {n:i for i, n in enumerate(inorder)}
        def dfs(il, ir, pl, pr):
            if il > ir or pl > pr:
                return None

            root_val = postorder[pr]
            if root_val not in pos_map:
                return None
            root = TreeNode(root_val)
            root_pos = pos_map[root_val]
            left_size = root_pos - il
            left = dfs(il, root_pos-1, pl, pl+left_size-1)
            right = dfs(root_pos+1, ir, pl+left_size+1, pr-1)
            root.left = left
            root.right = right
            return root

        return dfs(0, len(inorder)-1, 0, len(inorder)-1)
