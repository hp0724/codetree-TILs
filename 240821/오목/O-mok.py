n = 19
arr = [] 
for _ in range(n) :
    arr.append(list(map(int,input().split())))

white_win = False
black_win = False
result = []

for i in range(n):
    for j in range(n):
        # 검정돌 가로 
        if  j <= n-5 and arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i][j+2] == 1 and arr[i][j+3] == 1 and arr[i][j+4] == 1:
            black_win = True
            result = [i+1,j+3] 
        # 검정돌 세로 
        elif i <= n-5 and arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i+2][j] == 1 and arr[i+3][j] == 1 and arr[i+4][j] == 1:
            black_win = True
            result = [i+3,j+1] 
        # 검정돌 오른쪽 아래 대각선 
        elif i <=n-5 and j <=n-5 and arr[i][j] == 1 and arr[i+1][j+1] == 1 and arr[i+2][j+2] == 1 and arr[i+3][j+3] == 1 and arr[i+4][j+4] == 1:
            black_win = True
            result = [i+3,j+3]
        # 검정동 오른쪽 윗 대각선
        elif i >= 5 and j <=n-5 and arr[i][j] == 1 and arr[i-1][j+1] == 1 and arr[i-2][j+2] == 1 and arr[i-3][j+3] == 1 and arr[i-4][j+4] == 1:
            black_win = True
            result = [i-1,j+3]

        # 흰색돌 가로 
        elif j <= n-5 and arr[i][j] == 2 and arr[i][j+1] == 2 and arr[i][j+2] == 2 and arr[i][j+3] == 2 and arr[i][j+4] == 2:
            white_win = True 
            result = [i+1,j+3] 
        # 흰색돌 세로 
        elif i <= n-5 and arr[i][j] == 2 and arr[i+1][j] == 2 and arr[i+2][j] == 2 and arr[i+3][j] == 2 and arr[i+4][j] == 2:
            white_win = True 
            result = [i+3,j+1]
        # 흰색돌 오른쪽 아래 대각선  
        elif i <=n-5 and j <=n-5 and arr[i][j] == 2 and arr[i+1][j+1] == 2 and arr[i+2][j+2] == 2 and arr[i+3][j+3] == 2 and arr[i+4][j+4] == 2:
            white_win = True
            result = [i+3,j+3] 
        # 흰색돌 오른쪽 윗 대각선
        elif  i >= 5 and j <=n-5 and arr[i][j] == 2 and arr[i-1][j+1] == 2 and arr[i-2][j+2] == 2 and arr[i-3][j+3] == 2 and arr[i-4][j+4] == 2:
            white_win = True
            result = [i-1,j+3]

if black_win == False and white_win == False :
    print(0)
elif black_win == True:
    print(1)
    print(result[0], result[1])
elif white_win == True:
    print(2)
    print(result[0],result[1])