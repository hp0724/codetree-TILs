dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

total_cnt = 0
for y in range(len(array)):
    for x in range(len(array[0])):
        cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < len(array[0]) and 0 <= ny < len(array):
                if array[nx][ny] == 1:
                    cnt += 1
        if cnt >= 3:
            total_cnt += 1 
        
        

print(total_cnt)