import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	x, y, z = map(int, input().split())
	graph[x].append((y,z))
distance = [INF] * (n+1)

q = []
distance[c] = 0
heapq.heappush(q, (0, c))
while q:
	dist, now = heapq.heappop(q)
	if distance[now] < dist:
		continue
	for i in graph[now]:
		cost = distance[now] + i[1]
		if cost < distance[i[0]]:
			distance[i[0]] = cost
			heapq.heappush(q, (cost, i[0]))

count = 0
time = 0
for i in distance:
	if i==INF or i==0:
		continue
	else:
		count += 1
		if i > time:
			time = i
		
print(count, time)
	

