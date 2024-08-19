# N개의 방 시계 반대 방향으로 번호가 새겨져 있음
# 각 방에는 이웃한 두개의 방으로 통하는 문 
# 이중 for 문인데 한칸씩 이동하면 
n = int(input())
arr = []
result = 1e9 
for _ in range(n):
    arr.append(int(input()))


for i in range(n): 
    temp_result = 0
    for j in range(n):
        diff = (j-i+n) % n 
        temp_result += diff * arr[j]
    result = min(result,temp_result)

print(result)