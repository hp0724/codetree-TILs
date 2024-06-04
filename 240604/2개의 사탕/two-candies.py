# 빨간색 사탕을 밖으로 뺴려고 한다. 
# 사탕을 밖으로 뺴기 위해서 상자를 위 아래 왼쪽 오른쪽 방향으로 기울일수 있다. 
# 사탕은 장애물 혹은 다른 사탕에 부딪히기 전까지 미끌어지게 된다. 
# 파란색 사탕이 밖으로 나와서는 안된다. 
# 빨간색 사탕을 밖으로 빼내기 위해 기울여야 하는 최소 횟수를 구하시오 

import sys 
input = sys.stdin.readline 
from collections import deque

def getInput():
    n,m = map(int,input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(str, input())))

    for r in range(n):
        for c in range(m):
            if graph[r][c] == 'R':
                red = (r,c)
                graph[r][c] = '.'
            elif graph[r][c] == 'B':
                blue = (r,c)
                graph[r][c] = '.'
    
    return n,m,graph,red,blue 

def gravity(red,blue,direction):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    check = 0  # 빨강이 들어가면 1 파랑이 들어가면 2

    red_x,red_y = red 
    blue_x,blue_y = blue 
    is_other_exist = False # 다른 구슬이 있는가?? 

    while True:
        red_nx , red_ny = red_x + dx[direction] , red_y + dy[direction]

        if graph[red_nx][red_ny] == ".":
            if (red_nx,red_ny) == blue:
                is_other_exist = True
            red_x,red_y = red_nx,red_ny 
        elif graph[red_nx][red_ny] == '#':
            if is_other_exist:
                red_x ,red_y = red_x - dx[direction] , red_y - dy[direction]
                break 
            else:
                break
        elif graph[red_nx][red_ny] == 'O':
            check += 1
            break
    
    is_other_exist = False
    while True:
        blue_nx, blue_ny = blue_x + dx[direction] , blue_y + dy[direction]

        if graph[blue_nx][blue_ny] == ".":
            if (blue_nx,blue_ny) == red:
                is_other_exist = True
            blue_x,blue_y = blue_nx,blue_ny
        elif graph[blue_nx][blue_ny] == "#":
            if is_other_exist:
                blue_x ,blue_y = blue_x -dx[direction], blue_y - dy[direction]
                break
            else :
                break
        elif graph[blue_nx][blue_ny] == 'O':
            check += 2 
            break
    return (red_x,red_y),(blue_x,blue_y),check
    


n,m,graph,red,blue = getInput()
q = deque([(red,blue,0)])

flag = False
while q:
    r,b,turn = q.popleft()
    if turn == 10:
        continue

    for i in range(4):
        nr,nb,check = gravity(r,b,i)
        if check == 0:
            q.append((nr,nb,turn+1))
        elif check == 1:
            print(turn+1)
            flag = True
            break 
    if flag:
        break
else:
    print(-1)