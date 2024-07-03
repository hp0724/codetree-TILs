n,t = map(int,input().split())
arr = list(map(int,input().split()))

max_cnt = 0 
cnt = 1 
for i in range(1,n):
    if arr[i] > arr[i-1]:
        if arr[i-1] > t:
            cnt += 1
        else:
            cnt = 1
    else:
        cnt = 1
    max_cnt = max(max_cnt,cnt)


print(max_cnt)