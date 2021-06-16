'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

virus = []
for i in range(n):
    for j in range(m):
        if graph[n][m]==2:
            virus.append((n,m))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    queue = deque((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + dx[i]
            dy = x + dy[i]
            if dx<0 or dy<0 or dx>=n or dy>=m:
                continue
            if graph[dx][dy] == 1:
                continue
            if graph[dx][dy] == 0:
                queue.append((dx,dy))
                graph[dx][dy] = 2

for i in virus:
    bfs(i)

for i in graph:
    print(i)
