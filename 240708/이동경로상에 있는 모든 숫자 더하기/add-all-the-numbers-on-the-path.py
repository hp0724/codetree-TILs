N,T = map(int,input().split())
cmd_array = list(map(str,input()))

arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

x = N//2
y = N//2 
 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cur_direection = 0

result = arr[x][y]
def in_range(x,y):
    return 0 <= x < N and 0 <= y < N 

for c in cmd_array:
    if c == "R":
        cur_direection += 1 
        if cur_direection > 3 :
            cur_direection -= 4 
    elif c == "L":
        cur_direection -= 1 
        if cur_direection < 0 :
            cur_direection += 4 
    elif c == "F":
        nx = x + dx[cur_direection]
        ny = y + dy[cur_direection]

        if in_range(nx,ny):
            x = nx 
            y = ny 
            result += arr[x][y]
print(result)