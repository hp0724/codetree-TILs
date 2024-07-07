N = int(input())
x = 0
y = 0
dx = [-1,0,0,1]
dy = [0,-1,1,0]
for _ in range(N):
    d,c = input().split()
    c = int(c)
    for _ in range(c):
        if d == "W":
            x += dx[0]
            y += dy[0]

        elif d == "S":
            x += dx[1]
            y += dy[1]

        elif d == "N":
            x += dx[2]
            y += dy[2]

        elif d == "E":
            x += dx[3]
            y += dy[3]

print(x,y)