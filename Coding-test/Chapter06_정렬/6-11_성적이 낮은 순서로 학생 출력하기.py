data = []
n = int(input())
for i in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1])))

data = sorted(data, key=lambda student: student[1])

for student in data:
    print(student[0], end=' ')