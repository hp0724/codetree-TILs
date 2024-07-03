n = int(input())
result_array = []
cnt = 1
idx = 0
a = []
for _ in range(n):
    a.append(int(input()))

for i in range(1,n):
    if n == 1:
        result_array.append(cnt)
    if a[i] == a[i-1]:
        cnt+=1 
    else:
        result_array.append(cnt)
        cnt = 0
    # print(a)
    # print(result_array)


print(max(result_array)+1)