n,m = map(int,input().split())

answer = [[0]*(m) for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m 

dx = [0,1,0,-1]
dy = [1,0,-1,0]
x,y = 0,0 
dir_num = 0 # 0 :오른쪽 , 1:아래쪽 ,2:왼쪽 , 3:위쪽 

answer[x][y] = 1

for i in range (2,n*m +1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    # 더이상 나아갈수 없는 경우 
    if not in_range(nx,ny) or answer[nx][ny]!=0:
        dir_num = (dir_num+1) % 4 
    
    x += dx[dir_num]
    y += dy[dir_num]
    answer[x][y] = i
    

for i in range(n):
    for j in range(m):
        print(answer[i][j],end = " " )
    print()