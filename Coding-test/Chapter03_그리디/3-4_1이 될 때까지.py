n, k = map(int, input().split())
result = 0

while(n != 1):
    if n%k:
        n -= 1
    else:
        n /= k
    result += 1

print(result)