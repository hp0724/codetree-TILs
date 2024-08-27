import sys 
n = int(input())


arr = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
min_value = sys.maxsize
for i in range(n):
    for j in range(n):
        if j == i:
            continue 
        temp = (arr[i][0] -arr[j][0])* (arr[i][0] -arr[j][0])  + (arr[i][1] -arr[j][1]) *  (arr[i][1] -arr[j][1])
    min_value = min(min_value,temp)

print(min_value)