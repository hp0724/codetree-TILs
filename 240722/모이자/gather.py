n = int(input())
arr = list(map(int,input().split()))
max_sum = 0 
result = []
for i in range(n):
    sum_diff = 0 
    for j in range(n):
        sum_diff += arr[j]*abs(i-j)
    result.append(sum_diff)

print(min(result))