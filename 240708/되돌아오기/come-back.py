x = 0
y = 0

N = int(input())

mapper ={
    "N": 0,
    "E": 1,
    "W": 2,
    "S": 3
}

dx = [-1,0,0,1]
dy = [0,1,-1,0]

cnt = 0
sum_c = 0
for _ in range(N):
    d,c = input().split()
    c = int(c)
    sum_c += c 
    for _ in range(c):
        x += dx[mapper[d]]
        y += dy[mapper[d]]
        cnt += 1 
        if x == 0 and y == 0 :
            break 

    if x== 0 and y == 0:
        break

print(cnt)
if x!=0 and y!=0:
    print(-1)