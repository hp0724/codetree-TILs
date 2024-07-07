# K번이상 벌칙을 받게되면 벌금 

N,K,M = map(int,input().split())

array= [0]*(N+1)

result = -1 
for i in range(K):
    idx = int(input())
    array[idx] += 1
    if array[idx] == M:
        print(idx) 
        break 
else:
    print(result)