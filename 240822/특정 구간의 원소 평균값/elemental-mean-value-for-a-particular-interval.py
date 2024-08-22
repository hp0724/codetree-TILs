n = int(input())
arr = list(map(int,input().split()))
max_sum = 0 
cnt = 0
temp = []
for i in range(n):
    for j in range(i,n):
        sum_value = 0 
        for k in range(i,j+1):
            temp.append(arr[k])
        avg_value = sum(temp) / len(temp)
        if avg_value in temp:
            cnt += 1 
        temp = []
        

print(cnt)