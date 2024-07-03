n = int(input())
array = []
result_array = [0]*(2000)
offset = 1000
for _ in range(n):
    cnt,direction = input().split()
    array.append((cnt,direction))

pos = 1000 
for c,d in array:
    c = int(c)
    if d == 'R':
        for i in range(pos,pos+c):
            result_array[i]+=1 
        pos = pos + c 
    elif d == 'L':
        for i in range(pos-c,pos):
            result_array[i]+=1 
        pos = pos - c 

cnt = 0
for i in range(2000):
    if result_array[i] > 1:
        cnt += 1 

print(cnt)