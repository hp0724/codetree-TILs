n = int(input())
array = list(map(int,input().split()))
new_array = []
for i in range(len(array)):
    new_array.append((i+1,array[i]))

new_array.sort(key=lambda x:x[1])
new_new_array = []
for i in range(len(new_array)):
    new_new_array.append((new_array[i][0],i+1))

new_new_array.sort()
for i in range(len(new_new_array)):
    print(new_new_array[i][1],end=" ")