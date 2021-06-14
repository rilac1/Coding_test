n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start<=end):
	total = 0
	mid = (start + end) // 2
	
	for i in array:
		temp = i - mid
		if temp > 0:
			total += temp
	if total == m:
		result = mid
		break
	elif total < m:
		end = mid - 1
	else:
		start = mid + 1
		result = mid
	
print(result)

