# Description
# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room.

# We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that
# the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a gate, it should be filled with INF.

#  INF -1 INF  0
#  INF -1 INF  INF
#  INF -1  -1  0
#  0   -1   0  INF


from collections import deque

def wallsAndGates1(rooms):
    Map = {}

    def bfs(i ,j):
        q = deque([[i, j]])
        steps, reached = 0, False
        visited = set([(i, j)])
        nonlocal rooms, Map
        while q:
            sz = len(q)
            while sz:
                x, y = q.popleft()
                if rooms[x][y] == 0:
                    Map[(i, j)] = steps
                    reached = True
                    break
                for nx, ny in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                    if (0<=nx<m and 0<=ny<n
                                and rooms[nx][ny]!=-1
                                and (nx, ny) not in visited):
                        q.append([nx, ny])
                        visited.add((nx, ny))
                sz -= 1
            if reached:
                break
            steps += 1

    INF = 2**31 - 1
    m, n = len(rooms), len(rooms[0])
    for i in range(m):
        for j in range(n):
            if rooms[i][j]==INF:
                bfs(i, j)

    for p, s in Map.items():
        rooms[p[0]][p[1]] = s

    print(rooms)


def wallsAndGates1(rooms):
    m, n = len(rooms), len(rooms[0])
    # -1: wall  0: gate  INF: room
    levelQueue = deque((i, j)  for i in range(m) for j in range(n) if rooms[i][j] == 0)
    INF = 2**31-1
    while levelQueue:
        sz = len(levelQueue)
        steps = 0
        while sz:
            x, y = levelQueue.popleft()
            for nx, ny in ((x+1,y), (x-1,y),(x,y+1),(x,y-1)):
                if 0<=nx<m and 0<=ny<n and rooms[nx][ny]==INF:
                    rooms[nx][ny] = steps
                    







rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]










wallsAndGates1(rooms)

print(pairs)




