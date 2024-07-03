n = int(input())
result_array = []
cnt = 1
idx = 0
arr = []
for _ in range(n):
    arr.append(int(input()))
for i in range(n):
    if len(arr) == 1:
        result_array.append(arr[0])
        break
    elif arr[i] == arr[i-1]:
        cnt+=1 
    else:
        result_array.append(cnt)
        cnt = 0
if len(result_array) == 1:
    print(1)
else:
    print(max(result_array)+1)