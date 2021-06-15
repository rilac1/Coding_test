n, m = map(int, input().split())
money = []
for i in range(n):
	money.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in range(min(money), m+1):
	temp = []
	for j in money:
		if i-j >= 0:
			temp.append(d[i-j])
	d[i] = min(temp) + 1

if d[m]>10000:
	print("-1")
else:
	print(d[m])
