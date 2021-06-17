n, m = map(int, input().split())
graph = []
t_graph = [[0]*m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

def virus(x, y):
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if t_graph[nx][ny] == 0:
                t_graph[nx][ny] = 2
                virus(nx, ny)

def test():
    count = 0
    for i in range(n):
        for j in range(m):
            if t_graph[i][j]==0:
                count += 1
    return count

def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                t_graph[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if t_graph[i][j] == 2:
                    virus(i, j)
        result = max(result, test())
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)