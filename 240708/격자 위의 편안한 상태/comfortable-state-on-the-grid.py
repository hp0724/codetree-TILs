N,M = map(int,input().split())

arr = [[0]*N for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(M):
    x,y = map(int,input().split())
    x = x-1
    y = y-1 
    arr[x][y] = 1 
    cnt = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] ==1:
            cnt += 1 
        
    if cnt == 3:
        print(1)
    else:
        print(0)