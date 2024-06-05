# 0 ~9 까지의 임의의 숫자 
# n * m 격자판에 한 면이 1 * 1 크기인 정육면체 
# n , m , x, y , k 
# 지도 
# 굴리기 방향 

import sys
input = sys.stdin.readline

# 동 서 북 남 
dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]

dice = [0,0,0,0,0,0]

n,m,x,y,k = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

direction = list(map(int,input().split()))
if graph[y][x] == 0:
    graph[y][x] = dice[5]
    # 칸에 쓰여져 있는 수가 0이 아니면 , 칸에 쓰여져있는 수가 바닥면으로 복사 
    # 해당 칸의 수는 0 
elif graph[y][x] != 0:
    dice[5] = graph[y][x]
    graph[y][x] = 0

for d in direction:
    nx = x + dx[d]
    ny = y + dy[d]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue
    x = nx 
    y = ny 
    
    # 동쪽
    if d == 1:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4],dice[1],dice[0],dice[3],dice[5],dice[2] 
    # 서쪽
    elif d == 2:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[2],dice[1],dice[5],dice[3],dice[0],dice[4] 
    # 북쪽
    elif d == 3:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[1],dice[5],dice[2],dice[0],dice[4],dice[3] 
    # 남쪽 
    elif d == 4:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3],dice[0],dice[2],dice[5],dice[4],dice[1]     
    
    # 칸에 쓰여져 있는 수가 0이면 , 주사위의 바닥에 쓰여져있는 수가 칸에 복사 
    if graph[y][x] == 0:
        graph[y][x] = dice[5]
    # 칸에 쓰여져 있는 수가 0이 아니면 , 칸에 쓰여져있는 수가 바닥면으로 복사 
    # 해당 칸의 수는 0 
    elif graph[y][x] != 0:
        dice[5] = graph[y][x]
        graph[y][x] = 0

    print(dice[0])