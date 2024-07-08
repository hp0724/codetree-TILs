n = int(input())
arr = [[0]*n for _ in range(n)]
x = n//2 
y = n//2 
cur_direction = 0 
move_num = 1

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def in_range(x,y):
    return 0<= x < n and 0 <= y < n 

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def end():
    return not in_range(x,y)

cnt = 1 

while not end():
    for _ in range(move_num):
        arr[x][y] = cnt 
        cnt += 1 
        
        x += dx[cur_direction]
        y += dy[cur_direction]

        if end():
            break
    
    cur_direction = (cur_direction+1) % 4 
    
    if cur_direction == 0 or cur_direction == 2:
        move_num += 1 

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()