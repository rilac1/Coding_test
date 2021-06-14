print()
print()
n = int(input())
array = [0] * 100001
for i in input().split():
	array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))
tf = ["no", "yes"]
for i in x:
	print(tf[array[i]], end = ' ')


