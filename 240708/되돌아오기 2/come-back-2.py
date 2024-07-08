# 북쪽을 향한 상태
# L 왼쪽 90 
# R 오른쪽 90 
# F 앞으로 1칸
# 회전 ,이동 1초  
dx = [-1,0,1,0]
dy = [0,1,0,-1]
x = 0
y = 0

cur_dir = 0
cmd = list(map(str,input()))
cnt = 0

for c in cmd:
    if c == "F":
        x += dx[cur_dir]
        y += dy[cur_dir]
        cnt += 1
    elif c == "R":
        cur_dir += 1 
        if cur_dir > 3:
            cur_dir -= 4
        cnt += 1 
    elif c == "L":
        cur_dir -= 1 
        if cur_dir < 0:
            cur_dir += 4 
        cnt += 1
    if x == 0 and y == 0 :
        break 

if x == 0 and y == 0 :
    print(cnt)    
else:
    print(-1)