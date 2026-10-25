# No.116 connect right node
# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL。


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
from typing import Optional


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        if root:
            q.append(root)

        while q:
            sz = len(q)
            while sz:
                nxt = q.popleft()
                if sz!=1:
                    nxt.next = q[0]
                if nxt.left:
                    q.append(nxt.left)
                if nxt.right:
                    q.append(nxt.right)
                sz -= 1

        return root

    def connectByIterate(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        cur, nxt_level =  root, root.left
        while nxt_level:
            # connect current level
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next

            cur = nxt_level
            nxt_level = cur.left

        return root
