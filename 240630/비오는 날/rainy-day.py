n = int(input())
array = []
for _ in range(n):
    array.append((input().split()))

array.sort(key=lambda x:(x[2],x[0]))
print(" ".join(array[0]))