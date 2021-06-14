position = input()
column = (int(position[1]) - 1, ord(position[0]) - ord('a'))
count = 0

steps = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
for step in steps:
	x = column[0] + step[0]
	if (x<0 or x>7):
		continue
	y = column[1] + step[1]
	if (y<0 or y>7):
		continue
	count += 1

print(count)
