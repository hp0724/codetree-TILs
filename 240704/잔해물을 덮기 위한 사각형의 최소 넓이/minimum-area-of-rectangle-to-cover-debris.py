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
min_x1 = 1e6
min_y1 = 1e6
max_x2 = 0
max_y2 = 0
if temp:
    for x,y in temp:
        min_x1 = min(x,min_x1)
        min_y1 = min(y,min_y1)
        max_x2 = max(x,max_x2)
        max_y2 = max(y,max_y2)

    result_square_x = max_x2 - min_x1 + 1
    result_square_y = max_y2 - min_y1 + 1 

    print(result_square_x * result_square_y)
else:
    print(0)