arr = list(map(int,input().split()))

# 첫번째 팀의 합을 구해서 실시 
def get_diff(i,j,k):
    sum1 = arr[i] + arr[j] + arr[k]
    sum2 = sum(arr) - sum1 
    return abs(sum1-sum2)

min_diff = 1e9 

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            min_diff = min(min_diff,get_diff(i,j,k))

print(min_diff)