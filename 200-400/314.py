# No.314
# Description
# Given the root of a binary tree, return the vertical order traversal of its
# nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.



def traverVertical1(root):
    if not root:
        return []
    record = {}
    minWidth, maxWidth = float('inf'), float('-inf')

    def dfs(root, depth, width):
        if not root:
            return

        record[root] = [depth, width]
        nonlocal minWidth, maxWidth
        minWidth = min(minWidth, width)
        maxWidth = max(maxWidth, width)
        dfs(root.left, depth+1, width-1)
        dfs(root.right, depth+1, width+1)

    dfs(root, 0 ,0)
    w = maxWidth - minWidth + 1
    res = [[] for _ in range(int(w))]
    for n, pos in record.items():
        d, wi = pos[0], pos[1]
        res[wi-minWidth].append((d, n.val))
    # sorted in column

    for column in res:
        column.sort(key = lambda x: x[0])

    ul_res = []
    for column in res:
        ul_res.append([])
        for d, val in column:
            ul_res[-1].append(val)
    return ul_res


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.val = val

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.right=node4
node3.left=node5


res = traverVertical1(node1)

print(res)



# def traverVertical2(root):



d = {'s':'s', 3: 's','4':5}

print(d.items())