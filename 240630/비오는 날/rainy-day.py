n = int(input())
array = []
for _ in range(n):
    array.append((input().split()))

array.sort(key=lambda x:x[2])
print(" ".join(array[0]))