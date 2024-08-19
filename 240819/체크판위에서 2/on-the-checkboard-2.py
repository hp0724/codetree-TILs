# W 는 하얀색 B 는 검은색 
# 왼쪽 상단에서 우측 하단으로 이동할때 이동에 성공하는경우 
# 1. 점프 현재 색 != 점프 이후 적혀 있는 색
# 2. 점프 진행시 현재 위치에서 한칸 이상 오른쪽 AND 한칸 이상 아래쪽 
# 3. 도달한 위치가 정확히 2곳 
R,C= tuple(map(int,input().split()))
arr = []
for _ in range(R):
    arr.append((input().split()))
 
cnt = 0 

# arr[0][0]을 비어두기 
for i in range(1,R):
    for j in range(1,C):
        for k in range(i+1,R-1):
            for l in range(j+1,C-1):
                if arr[0][0] != arr[i][j] and arr[i][j] != arr[k][l] and arr[k][l] != arr[R-1][C-1]:
                        cnt += 1

print(cnt)