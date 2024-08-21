# N 개와 정수 S 
# N개의 수들 중 정확히 2개를 제외 하여 숫자의 합이 S 

N,S = map(int,input().split())

arr = list(map(int,input().split()))
min_value = 1e6
sum_arr = []

for i in range(N):
    for j in range(i+1,N):
        temp1 = arr.pop(i)
        temp2 = arr.pop(j-1)
        sum_arr.append(sum(arr))
        arr.insert(i,temp1)
        arr.insert(j,temp2)

for s in sum_arr:
    min_value = min(min_value,abs(S-s))

print(min_value)