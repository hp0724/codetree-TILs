n,k = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0 
for i in range(n-k+1):
    max_value = 0 
    for j in range(i,i+k):
        max_value += arr[j]
    ans = max(ans,max_value)

print(ans)