"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        Map, q = {}, deque([node])
        visited = set()

        while q:
            top = q.popleft()

            if top in visited:
                continue
            visited.add(top)

            if top not in Map:
                Map[top] = Node(top.val)

            for n in top.neighbors:
                if n not in Map:
                    Map[n] = Node(n.val)
                Map[top].neighbors.append(Map[n])
                q.append(n)

        return Map[node]




