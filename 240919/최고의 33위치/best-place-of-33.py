N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

max_count = 0 
def count_coin(x,y):
    cnt = 0 
    for i in range(x,x+3):
        for j in range(y,y+3):
            if arr[i][j] == 1:
                cnt += 1 
    return cnt    

for i in range(N):
    for j in range(N): 
        if i+2 < N and j+2 <N : 
            max_count = max(max_count,count_coin(i,j))

print(max_count)