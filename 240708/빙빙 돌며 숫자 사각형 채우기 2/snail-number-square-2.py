n,m = map(int,input().split())
arr = [[0]*m for _ in range(n)]
x = 0
y = 0 
arr[x][y] = 1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cur_direction = 0
def in_range(x,y):
    return 0 <= x < n and 0<= y <m 
for i in range(2,n*m +1):
    nx = x + dx[cur_direction]
    ny = y + dy[cur_direction]
    if not in_range(nx,ny) or arr[nx][ny] !=0:
         cur_direction = (cur_direction+1) % 4 

    x = x + dx[cur_direction]
    y = y + dy[cur_direction]
    arr[x][y] = i

for a in arr:
    print(" ".join(map(str,a)))