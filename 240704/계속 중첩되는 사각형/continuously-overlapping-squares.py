# 빨간색, 파란색 순으로 번갈아 가며
# 빨간 = 0 
# 파란 = 1
n = int(input())
OFFSET = 100 
MAX_R = 200

square = [[9]*MAX_R for _ in range(MAX_R)]
for k in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    x1 += OFFSET
    y1 += OFFSET 
    x2 += OFFSET
    y2 += OFFSET

    k = k%2 

    for i in range(x1,x2):
        for j in range(y1,y2):
            square[i][j] = k 

cnt = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if square[i][j] == 1:
            cnt += 1 

print(cnt)