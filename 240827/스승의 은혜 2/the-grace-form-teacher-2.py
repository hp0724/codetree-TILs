# N 명의 학생에게 B 만큼의 예산으로 선물 
# 학생 I가 원하는 선물의 가격 P(i)

N,B = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
i = 0 
cnt = 0
print(arr)
while B > 0 and i < len(arr):
    if arr[i] >= B :
        if arr[i] // 2  <= B :
            B -= arr[i] //2
            cnt += 1
    else:
        B -= arr[i]
        cnt+=1 
    i += 1 

print(cnt)