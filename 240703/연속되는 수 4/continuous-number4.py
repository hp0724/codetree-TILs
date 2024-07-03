n = int(input())
arr = []
for _ in range(n): 
    arr.append(int(input()))

cnt = 1
max_cnt = 0
for i in range(n):
    if arr[i] > arr[i-1]:
        cnt += 1 
    else: 
        max_cnt = max (cnt,max_cnt)
        cnt = 1

print(max_cnt)