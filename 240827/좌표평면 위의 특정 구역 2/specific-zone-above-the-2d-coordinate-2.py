# N개의 점들 중 정확히 하나의 점만 빼서 모든 점들을 포함하는 직사각형의 넓이를 최소 
n = int(input())
arr = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))



ans = 1e6

for i in range(n):
    min_x = 1e6
    min_y = 1e6
    max_x = 0 
    max_y = 0 
    for j in range(n):
        if j == i :
            continue 
        min_x = min(min_x,arr[j][0])
        min_y = min(min_y,arr[j][1])
        max_x = max(max_x,arr[j][0])
        max_y = max(max_y,arr[j][1])

         
    # 배열중에서 최대값 
    square = (max_x - min_x) * (max_y - min_y)
    # 선분 1개씩 뺀 경우에 최대값중에서 최소 
    ans = min(ans,square)

print(ans)