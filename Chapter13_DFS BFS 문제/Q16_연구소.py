from collections import deque
import itertools

def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = 2

def test(graph):
    count = 0
    for i in virus:
        bfs(graph, i[0], i[1])

    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                count += 1
    return count

# n, m = map(int, input().split())
n, m = 7, 7
graph = []
graph = [
    [2,0,0,0,1,1,0],
    [0,0,1,0,1,2,0],
    [0,1,1,0,1,0,0],
    [0,1,0,0,0,0,0],
    [0,0,0,0,0,1,1],
    [0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0]
]
'''
for i in range(n):
    graph.append(list(map(int, input().split())))
'''

virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            virus.append((i,j))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0
for i in itertools.permutations(list(range(n*m)),3):
    t_graph = graph
    for j in i:
        x = j//n
        y = j % m
        if t_graph[x][y]==0:
            break
        t_graph[x][y] = 1
    result = max(result, test(t_graph))

print(result)

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
