# No. 298 Binary Tree Longeset Consecutive Sequence

# 给你一棵指定的二叉树的根节点 root，请你计算其中 最长连续序列路径 的长度。

# 最长连续序列路径 是依次递增 1 的路径。该路径，可以是从某个初始节点到树中任意节点，通过「父 - 子」关系连接而产生的任意路径。
# 且必须从父节点到子节点，反过来是不可以的。


class Solution:
    def longestConsecutive(self, root) -> int:
        
