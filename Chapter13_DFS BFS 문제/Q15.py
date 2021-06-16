# n: 도시 개수, m: 도로 개수, k: 거리 정보, x: 출발 도시

n, m, k, x = map(int, input().split())
graph = [[] for _ in range (n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

visited = [False]*(n+1)
queue = [[],[]]
queue[0].append(x)
visited[x] = True
t = 0

while queue[0] or queue[1]:
    v = queue[t%2].pop(0)
    for i in graph[v]:
        if not visited[i]:
            queue[(t+1)%2].append(i)
            visited[i] = True
    if not queue[t%2]:
        t += 1
    if t==k:
        break
print("t: %d" %t)

if len(queue[k%2]) > 0:
    for i in queue[k%2]:
        print(i)
else:
    print("-1")