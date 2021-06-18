import heapq

c, n = map(int, input().split())
house = []
for _ in range(n):
    heapq.heappush(house, int(input()))