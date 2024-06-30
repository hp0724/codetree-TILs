n,k,T = input().split()
n = int(n)
k = int(k)
array = []
result = []
for _ in range(n):
    array.append(input())

for i in array:
    if i.startswith(T): 
        result.append(i)

result.sort()
print(result[k-1])