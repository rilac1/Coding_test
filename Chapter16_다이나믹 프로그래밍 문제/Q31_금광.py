n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

def d(a,b):
    if a>=n or a<0 or b>=m or b<0:
        return 0
    else:
        return data[a][b]

for j in range(1,m):
    for i in range(n):
        data[i][j] += max(d(i-1, j-1), d(i,j-1), d(i+1, j-1))

# 마지막 열만 추출하기
result = [i [m-1] for i in data]
print(max(result))