def binary_search(array, target):
	start = 0
	end = len(array) - 1
	while start <= end:
		mid = (start + end) // 2
		if array[mid] == target:
			return 1
		elif array[mid] > target:
			end = mid - 1
		else:
			start = mid + 1
	return 0

print()
print()
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split()))

tf = ["no", "yes"]
for i in x:
	print(tf[binary_search(array, i)], end = ' ')
