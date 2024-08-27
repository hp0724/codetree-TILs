import sys 
n = int(input())

arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

min_value = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        temp = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2
        min_value = min(min_value, temp)

print(min_value)