import sys 
input = sys.stdin.readline
n = int(input())
max_cnt = 0
arr = []
cnt = 1

for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    if arr[i] > 0 and arr[i-1] > 0:
        cnt += 1 
    elif arr[i] < 0 and arr[i-1] <0:
        cnt += 1 
    else:
        max_cnt = max(max_cnt,cnt)
        cnt = 1

print(max_cnt)