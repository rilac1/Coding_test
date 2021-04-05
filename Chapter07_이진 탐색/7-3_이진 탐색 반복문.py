def binary_serch(array, target):
	start = 0
	end = len(array) - 1
	while start <= end:
		mid = (start + end) // 2
		if array[mid] == target:
			return mid + 1
		elif array[mid] > target:
			end = mid - 1
		else:
			start = mid + 1
print()
print("Input the target:")
target = int(input())
print("Input the array:")
array = list(map(int, input().split()))

result = binary_serch(array, target)
if result==None:
	print("no")
else:
	print(result)
