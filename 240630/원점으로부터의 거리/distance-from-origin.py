n = int(input())
array = []
for i in range(n):
    x,y = map(int,input().split())
    distance = abs(x-0) + abs(y-0)
    array.append((i+1,distance))

array.sort(key=lambda x:x[1])
for i in array:
    print(i[0])