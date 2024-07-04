OFFSET = 1000 
MAX_R = 2000 
square = [[0]*MAX_R for _ in range(MAX_R)]
for k in range(1,3):
    x1,y1,x2,y2 = map(int,input().split())
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET 

    for i in range(x1,x2):
        for j in range(y1,y2):
            square[i][j] = k 

cnt = 0 
temp = []
for i in range(MAX_R):
    for j in range(MAX_R):
        if square[i][j] == 1 :
            temp.append((i,j))
if temp:
    x1_min ,y1_min = min(temp)
    x2_max ,y2_max = max(temp)

    result_square_x = x2_max - x1_min + 1
    result_square_y = y2_max - y1_min + 1 

    print(result_square_x * result_square_y)
else:
    print(0)