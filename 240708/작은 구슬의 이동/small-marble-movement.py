n,t = map(int,input().split())
r,c,d = input().split()
r = int(r)
c= int(c)

array = [[0]*n for _ in range(n)]
mapper = {
    "R" : 0 ,
    "D" : 1,
    "U" : 2,
    "L" : 3
}
dx = [0,-1,1,0]
dy = [1,0,0,-1]
cnt = 0
dir_num = mapper[d]



while cnt != t+1:
    nx = r + dx[dir_num] 
    ny = c + dy[dir_num]
    if nx < 0 or nx >=n or ny < 0 or ny >=n:
        dir_num = 3 - dir_num
        cnt += 1
    
    r = r + dx[dir_num] 
    c = c + dy[dir_num]
    cnt += 1
    
print(r,c)