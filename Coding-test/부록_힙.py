import heapq

def heapsort(iterable):
	h = []
	result = []
	# 모든 원소를 차례대로 힙에 삽입
	for value in iterable:
		heapq.heappush(h, value)
	# 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
	for i in range(len(h)):
		result.append(heapq.heappop(h))
	return result
	
def max_heapsort(iterable):
	h = []
	result = []
	for value in iterable:
		heapq.heappush(h, -value)
	for i in range(len(h)):
		result.append(-heapq.heappop(h))
	return result

array = [1, 3, 5, 7, 9, 6, 8, 0]
result = heapsort(array)
result2 = max_heapsort(array)
print(result)
print(result2)
