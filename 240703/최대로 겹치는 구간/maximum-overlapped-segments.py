n = int(input())
MAX_VALUE = 101
OFFSET = 100
array = [0]*(MAX_VALUE+OFFSET)
for _ in range(n):
    x1,x2 = map(int,input().split())
    for i in range(x1+OFFSET,x2+OFFSET):
        array[i] += 1 

print(max(array))