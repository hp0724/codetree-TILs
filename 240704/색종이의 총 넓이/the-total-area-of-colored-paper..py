MAX_R = 200 
OFF_SET = 100 
square = [[0]*MAX_R for _ in range(MAX_R)]
n = int(input())
for _ in range(n):
    x1,y1 = map(int,input().split())
    x1 += OFF_SET
    y1 += OFF_SET 
    x2 = x1 + 8 
    y2 = y1 + 8 

    for i in range(x1,x2):
        for j in range(y1,y2):
            square[i][j] = 1 
            
cnt = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if square[i][j] == 1:
            cnt += 1 

print(cnt)