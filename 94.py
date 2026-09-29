# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal1(self, root: TreeNode | None) -> list[int]:
        st, res = [], []
        cur = root

        while cur or st:
            if cur:
                while cur:
                    st.append(cur)
                    cur = cur.left
            top = st.pop()
            res.append(top.val)
            cur = top.right

        return res
    def inorderTraversal2(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        left = self.inorderTraversal1(root.left)
        right = self.inorderTraversal1(root.right)

        res = []
        res.extend(left)
        res.append(root.val)
        res.extend(right)

        return res

root1 = TreeNode(1)
root2 = TreeNode(2)
root3 = TreeNode(3)
root4 = TreeNode(4)
root5 = TreeNode(5)
root6 = TreeNode(6)

root1.left = root2
root1.right = root3
root2.left = root4
root2.right = root5
root3.left = root6

#          1
#      2        3
#   4     5   6


print(Solution().inorderTraversal1(root1))
print(Solution().inorderTraversal2(root1))


