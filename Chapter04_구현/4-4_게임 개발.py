import time

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
stage = []
visited = [(x,y)]
for i in range(n):
	stage.append(list(map(int, input().split())))
start = time.time()
steps = [(-1,0), (0,1), (1,0), (0,-1)]

while True:
	turn = 0
	while (turn < 4):
		direction -= 1
		if direction < 0:
			direction = 3
		step = steps[direction]
		dx = x + step[0]
		dy = y + step[1]
		if stage[dx][dy]==0 and (dx,dy) not in visited:
			x, y = dx, dy
			visited.append((x,y))
			turn = 0
		else:
				turn += 1
	x -= step[0]
	y -= step[1]
	if stage[dx][dy]:
		break


print(len(visited))
print("time: ", time.time() - start)
