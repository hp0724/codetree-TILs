# 다른 선분과 전혀 곂치치 않는 선분의 수를 출력 
# 선분이 곂치는 경우는 총 2가지 
# x1이 크고 x2가 작은경우 
# x1이 작고 x2가 큰경우 
n = int(input())

arr = []
ans = 0
for _ in range(n):
    x1,x2 = map(int,input().split())
    arr.append((x1,x2))


for i in range(n):
    overlap = False 
    for j in range(n):
        if j == i :
            continue 
        if (arr[i][0] <= arr[j][0] and arr[i][1] >= arr[j][1]) or (arr[i][0] >= arr[j][0] and arr[i][1] <= arr[j][1]):
            overlap = True
            break 
    if overlap == False:
        ans += 1 
print(ans)