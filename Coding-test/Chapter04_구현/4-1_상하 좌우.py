n = int(input())
x, y = 1, 1
plans = input().split()

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for plan in plans:
	i = move_types.index(plan)
	nx = x + dx[i]
	ny = y + dy[i]
	if (nx>0 and nx<n):
		x = nx
	if (ny>0 and ny<n):
		y = ny

print(x, y)	
