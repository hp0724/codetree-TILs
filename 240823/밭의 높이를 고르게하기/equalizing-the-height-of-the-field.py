#  N개의 밭의 높이가 주어지면 연속하게 최소 T번 이상 H높이로 나오게끔 하려고 할 때
N,H,T = map(int,input().split())

arr = list(map(int,input().split()))

min_value = 1e6
for i in range(N):
    for j in range(i+T,N):
        temp = 0
        for k in range(i,j):
            temp += abs(H-arr[k])
        min_value = min(min_value,temp)

print(min_value)