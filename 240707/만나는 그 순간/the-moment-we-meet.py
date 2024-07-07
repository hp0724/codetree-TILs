N,M = map(int,input().split())
a_arr = []
b_arr = []
a_sum_count = 0 
b_sum_count = 0
for _ in range(N):
    direction , count = input().split()
    a_arr.append((direction,int(count)))

for _ in range(M):
    direction,count = input().split()
    b_arr.append((direction,int(count)))

for_count = max(a_sum_count,b_sum_count)

a_result_arr = [0]
for d,c in a_arr :
    if d == 'R':
        for i in range(c):
            a_result_arr.append(a_result_arr[-1]+1)
    if d == 'L':
        for i in range(c):
            a_result_arr.append(a_result_arr[-1]-1)

b_result_arr = [0]
for d,c in b_arr:
    if d == 'R':
        for i in range(c):
            b_result_arr.append(b_result_arr[-1]+1)
    if d == 'L':
        for i in range(c):
            b_result_arr.append(b_result_arr[-1]-1)

idx = 1 

while True:
    if a_result_arr[idx] == b_result_arr[idx]:
        print(idx)
        break
    idx += 1