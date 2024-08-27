n = int(input())

arr = []

for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))

max_result = 0 
# x축에 평행하거나 y축에 평행한경우 
# (0,0), (1,0), (1,2)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            result = 0
            if arr[i][0] - arr[j][0] == 0 and arr[j][1] - arr[k][1] == 0 :
                result = abs(arr[i][1] - arr[j][1]) * abs(arr[j][0] - arr[k][0])
                max_result = max(max_result,result)

            if arr[i][0] - arr[k][0] == 0 and arr[k][1] - arr[j][1] == 0 :
                result = abs(arr[i][1] - arr[k][1]) * abs(arr[k][0] - arr[j][0])
                max_result = max(max_result,result)

            if arr[j][0] - arr[i][0] == 0 and arr[i][1] - arr[k][1] == 0 :
                result = abs(arr[j][1] - arr[i][1]) * abs(arr[i][0] - arr[k][0])
                max_result = max(max_result,result)

            if arr[j][0] - arr[k][0] == 0 and arr[k][1] - arr[i][1] == 0 :
                result = abs(arr[j][1] - arr[k][1]) * abs(arr[k][0] - arr[i][0])
                max_result = max(max_result,result)

            if arr[k][0] - arr[i][0] == 0 and arr[i][1] - arr[j][1] == 0 :
                result = abs(arr[k][1] - arr[i][1]) * abs(arr[i][0] - arr[j][0])
                max_result = max(max_result,result)

            if arr[k][0] - arr[j][0] == 0 and arr[j][1] - arr[i][1] == 0 :
                result = abs(arr[k][1] - arr[j][1]) * abs(arr[j][0] - arr[i][0])
                max_result = max(max_result,result)


print(max_result)