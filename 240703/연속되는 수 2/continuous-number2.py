n = int(input())
result_array = []
cnt = 1
idx = 0
arr = []
for _ in range(n):
    arr.append(int(input()))

if n == 1:
    print(1)
else:
    for i in range(1,n):
        if len(arr) == 1:
            result_array.append(arr[0])
            break
        elif arr[i] == arr[i-1]:
            cnt+=1 
            if i == n-1:
                result_array.append(cnt)
        elif arr[i] != arr[i-1]:
            result_array.append(cnt)
            cnt = 1
        # print(result_array)
    print(max(result_array))