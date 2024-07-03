n = int(input())
offset = 100 
array = [[0]*200 for _ in range(200)]

for _ in range(n):
    x1,y1,x2,y2 = list(map(int,input().split()))
    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset
    for i in range(x1,x2):
        for j in range(y1,y2):
            if array[i][j] == 0:
                array[i][j] = 1 
cnt = 0
for i in range(200):
    for j in range(200):
        if array[i][j] == 1:
            cnt += 1

print(cnt)