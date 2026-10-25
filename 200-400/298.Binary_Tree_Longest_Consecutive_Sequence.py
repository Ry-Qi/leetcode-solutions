# No. 298 Binary Tree Longeset Consecutive Sequence

# 给你一棵指定的二叉树的根节点 root，请你计算其中 最长连续序列路径 的长度。

# 最长连续序列路径 是依次递增 1 的路径。该路径，可以是从某个初始节点到树中任意节点，通过「父 - 子」关系连接而产生的任意路径。
# 且必须从父节点到子节点，反过来是不可以的。


class Solution:
    def longestConsecutive(self, root) -> int:
        if not root:
            return 0

        res = 0

        def dfs(root, prev, consecutive):
            nonlocal res
            if not root:
                return

            if prev+1 == root.val:
                res = max(res, consecutive+1)
                dfs(root.left, root.val,consecutive+1)
                dfs(root.right, root.val, consecutive+1)
            else:
                res = max(res, consecutive)
                dfs(root.left, root.val, 1)
                dfs(root.right, root.val, 1)

        dfs(root, float('-inf'), 1)
        return res

# No. 549 Binary Tree Longeset Consecutive Sequence 2
# 给定二叉树的根 root，返回树中最长连续路径的长度。
# 连续路径是路径中相邻节点的值相差 1 的路径。此路径可以是增加或减少。

# 例如， [1,2,3,4] 和 [4,3,2,1] 都被认为有效，但路径 [1,2,4,3] 无效。
# 另一方面，路径可以是子 - 父 - 子顺序，不一定是父子顺序。

class Solution:
    def longestConsecutive(self, root) -> int:

        res = 0

        def dfs(root, prev, up):
            if not root:
                return 0

            left_down = dfs(root.left, root.val,False)
            left_up = dfs(root.left, root.val,True)
            right_down = dfs(root.right, root.val,False)
            right_up = dfs(root.right, root.val,True)

            nonlocal res
            res = max(left_down + right_up + 1, res)
            res = max(left_up + right_down + 1, res)

            if up:
                if prev+1!=root.val:
                    return 0
                return max(left_up, right_up) + 1
            else:
                if prev-1!=root.val:
                    return 0
                return max(left_down, right_down) + 1

        dfs(root, root.val-1,True)
        dfs(root, root.val+1,False)

        return res

    def longestConsecutive2(self, root) -> int:
        res = 0
        def dfs(root):

            if not root:
                return 0, 0

            up, down = 1, 1
            if root.left:
                leftUp, leftDown = dfs(root.left)
                if root.val-1 == root.left.val:
                    down = max(down, leftDown+1)
                elif root.val+1 == root.left.val:
                    up = max(up, leftUp+1)

            upR, downR = 1, 1
            if root.right:
                rightUp, rightDown = dfs(root.right)
                if root.val+1 == root.right.val:
                    upR = max(upR, 1 + rightUp)
                elif root.val-1 == root.right.val:
                    downR = max(downR, 1 + rightDown)

            candidate =  max(max(up+downR-1, down+upR-1, 1), max(down+upR-1, up+downR-1, 1))
            nonlocal res
            res = max(res, candidate)
            return max(up, upR), max(down, downR)

        dfs(root)

        return res
