# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def preorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = [root.val]
        res.extend(self.preorderTraversal1(root.left))
        res.extend(self.preorderTraversal1(root.right))

        return res

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res, st = [], []
        cur = root

        while cur or st:
            while cur:
                res.append(cur.val)
                st.append(cur)
                cur = cur.left
            top = st.pop()
            cur = top.right
        
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


print(Solution().preorderTraversal1(root1))
print(Solution().preorderTraversal2(root1))
