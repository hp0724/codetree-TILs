# 1 부터 N 까지 숫자를 중복해서 뽑아 총 3자리 
# 총 조합의 수에서 안열리는 수 빼는것이 좋을듯 

N = int(input())
arr = list(map(int,input().split()))

for i in range(len(arr)):
    arr[i] += 3

cnt = 0 
total_combi = N*N*N 

cnt = 0
for i in range(arr[0],N+1):
    for j in range(arr[1],N+1):
        for k in range(arr[2],N+1):
            cnt += 1 

result = total_combi - cnt 

print(result)