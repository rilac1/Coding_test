n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

count = m//(k+1)
result = second * count + first * (m-count)
print(result)