# 236. Lowest Common Ancestor of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path = []
        def findPath(root, target):
            if not root:
                return

            path.append(root)
            if root is target: return True

            found = findPath(root.left, target)
            if found: return True
            found = findPath(root.right, target)
            if found: return True

            path.pop()
            return False

        findPath(root, p)
        p_path = path.copy()
        path = []
        findPath(root, q)
        q_path = path.copy()
        p_node = set(p_path)

        res = None
        for n in q_path:
            if n in p_node:
                res = n

        return res


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def countNode(root, p, q):
            if not root:
                return 0

            nonlocal res
            count = countNode(root.left, p, q) + countNode(root.right, p, q)
            if count == 2 and res is None:
                res = root
                return 2

            if root is p or root is q:
                if count==1:
                    res = root
                    return 2
                count += 1

            return count

        countNode(root, q, p)
        return res
