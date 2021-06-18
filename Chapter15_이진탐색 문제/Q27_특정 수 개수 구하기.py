from bisect import bisect_left, bisect_right
n, x = map(int, input().split())
data = list(map(int, input().split()))

def count_by_range(a, left_value, right_value):
    left = bisect_left(a, left_value)
    right = bisect_left(a, right_value)
    return right-left

count = count_by_range(data, x,x)

if count==0:
    print(-1)
else:
    print(count)