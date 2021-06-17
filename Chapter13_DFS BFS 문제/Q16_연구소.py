from collections import deque
import itertools
import copy

def bfs(graph):
    for i in virus:
        x,y = i[0], i[1]
        queue = deque()
        queue.append((x,y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if graph[nx][ny] == 0:
                    queue.append((nx,ny))
                    graph[nx][ny] = 2

def test(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                count += 1
    return count

def dfs(count):
    global result
    if count == 0:
        result = 0
    if count==3:
        t_graph = copy.deepcopy(graph)
        bfs(t_graph)
        result = max(result, test(t_graph))
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                count -= 1
                graph[i][j] = 0


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            virus.append((i,j))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

dfs(0)
print(result)
