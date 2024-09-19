# n * n 격자 
# 행복한 수열 = 연속하여 m 개 이상의 동일한 원소가 나오는 순간이 존재하는 수열 
# 가로 세로만 고려 대각선 고려 안함 

n,m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

total_cnt = 0 

for i in range(n):
    cnt = 1
    for j in range(1,n):
        if arr[i][j-1] == arr[i][j]:
            cnt +=1 
        elif arr[i][j-1] != arr[i][j]:
            cnt = 0
        if cnt >= m :
            total_cnt +=1 
         

for i in range(n):
    cnt = 1
    for j in range(1,n):
        if arr[j-1][i] == arr[j][i]:
            cnt +=1 
        elif arr[j-1][i] != arr[j][i]:
            cnt = 0
        if cnt >= m :
            total_cnt +=1 

print(total_cnt)