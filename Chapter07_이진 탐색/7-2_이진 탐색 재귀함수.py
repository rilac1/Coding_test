def binary_search(array, target, start, end):
	if start > end:
		return None
	mid = (end + start) // 2
	if array[mid] == target:
		return mid + 1
	elif array[mid] > target:
		binary_search(array, target, start, mid-1)
	elif array[mid] < target:
		binary_search(array, target, mid+1, end)

print()
print("Input target:")
target = int(input())
print("Input array:")
array = list(map(int, input().split()))

result = binary_search(array, target, 0, len(array))

if result == None:
	print("No")
else:
	print(result)

