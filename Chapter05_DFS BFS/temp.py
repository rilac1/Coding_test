from collections import deque

dx = [-1,0,+1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split)))

