N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))

cnt = 0
for i in range(N):
    for j in range(M):
        # 왼쪽 -> 오른쪽 LEE
        if j <= M-3 and arr[i][j] == 'L' and arr[i][j+1] == 'E' and arr[i][j+2] == 'E':
            cnt += 1 
        # 오른쪽 -> 왼쪽 LEE
        if j >= 2 and arr[i][j] == 'L' and arr[i][j-1] == 'E' and arr[i][j-2] == 'E':
            cnt += 1
        # 위 -> 아래 LEE
        if i <= N-3 and arr[i][j] == 'L' and arr[i+1][j] == 'E' and arr[i+2][j] == 'E':
            cnt += 1
        # 아래 -> 위 LEE
        if i >=2 and arr[i][j] == 'L' and arr[i-1][j] == 'E' and arr[i-2][j] == 'E':
            cnt += 1  
        # 왼쪽 아래 대각선 -> 오른쪽 위 
        if i >= 2 and j <= M-3 and arr[i][j] == 'L' and arr[i-1][j+1] == 'E' and arr[i-2][j+2] == 'E':
            cnt += 1
        # 왼쪽 위 대각선 -> 오른쪽 아래 
        if i <= N-3 and j <= M-3 and arr[i][j] == 'L' and arr[i+1][j+1] == 'E' and arr[i+2][j+2] == 'E':
            cnt += 1
        # 오른쪽 위 -> 왼쪽 아래 대각선 
        if i <= N-3 and j >= 2 and arr[i][j] == 'L' and arr[i+1][j-1] == 'E' and arr[i+2][j-2] == 'E':
            cnt += 1
        # 오른쪽 아래 -> 왼쪽 위 대각선 
        if i >=2 and j>= 2 and arr[i][j] == 'L' and arr[i-1][j-1] == 'E' and arr[i-2][j-2] == 'E':
            cnt += 1

print(cnt)