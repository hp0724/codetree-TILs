n = int(input())
arr = list(map(int,input().split()))

max_value = 0 
for i in range(n-2):
    for j in range(i+1,n):
        temp = arr[i] + arr[j]
        max_value = max(max_value,temp)

print(max_value)