alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
"U","V","W","X","Y","Z"]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
cur_direction = 0

n,m = map(int,input().split())
x = 0
y = 0 
arr = [[0]*m for _ in range(n)]

arr[x][y] = "A"
def in_range(x,y):
    return 0 <= x < n and 0<= y < m 


for i in range(1,n*m):
    
    nx = x + dx[cur_direction]
    ny = y + dy[cur_direction]

    if not in_range(nx,ny) or arr[nx][ny] != 0 :
        cur_direction = (cur_direction+1) % 4

    x = x + dx[cur_direction]
    y = y + dy[cur_direction]

    arr[x][y] = alphabet[i % len(alphabet)]

    

for a in arr :
    print((" ".join(map(str,a))))