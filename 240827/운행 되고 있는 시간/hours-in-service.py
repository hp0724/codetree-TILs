n = int(input())
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
max_cnt = 0
for i in range(n):
    cnt_arr = [0] * 1001
    cnt = 0 
    for j in range(n):
        if i == j :
            continue 
        for k in range(arr[j][0],arr[j][1]):
            cnt_arr[k]+=1 
    for l in range(len(cnt_arr)):
        if cnt_arr[l] != 0 :
            cnt += 1 
    max_cnt = max(max_cnt,cnt)


print(max_cnt)