MAX_R = 2000
OFFSET = 1000
square = [[0]*MAX_R for _ in range(MAX_R)]
n = 4
for k in range(1,n):
    x1,y1,x2,y2 = map(int,input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    for i in range(x1,x2):
        for j in range(y1,y2):
            square[i][j] = k 

cnt = 0

for i in range(MAX_R):
    for j in range(MAX_R):
        if square[i][j]!=0 and square[i][j]!=3:
            cnt += 1

print(cnt )