n = int(input())
loc = list(map(int, input().split()))
loc.sort()
print(loc[(n-1)//2])