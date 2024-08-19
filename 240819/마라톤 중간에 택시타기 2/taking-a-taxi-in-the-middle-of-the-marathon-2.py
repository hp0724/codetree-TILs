# 1번 체크포인트 -> N번 체크포인트에서 끝나기 
# 1번하고 N번 빼고 체크포인트 건너뛰기 1개 가능 
# 맨하튼 거리로 계산 

n = int(input())
arr = []
result = 1e9
temp_result = 0
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))

for i in range(1,n-1):
    temp = arr.pop(i)
    for j in range(len(arr)-1):
        x1,y1 = arr[j]
        x2,y2 = arr[j+1]
        temp_result += (abs(x1-x2) + abs(y1-y2))
    result = min(result,temp_result)
    arr.insert(i,temp)
print(result)