N,M = map(int,input().split())

a_arr = [0]
b_arr = [0]
for _ in range(N):
    v,t = map(int,input().split())
    for _ in range(t):
        a_arr.append(a_arr[-1]+v)

for _ in range(M):
    v,t = map(int,input().split())
    for _ in range(t):
        b_arr.append(b_arr[-1]+v)

# print(a_arr)
# print(b_arr)

change_cnt = 0
for i in range(len(a_arr)):
    if a_arr[i] >= b_arr[i] and a_arr[i-1] < b_arr[i-1]:
        change_cnt += 1 
    elif b_arr[i] >= a_arr[i] and b_arr[i-1] < a_arr[i-1]:
        change_cnt += 1
if change_cnt == 0 :
    print(0)
else:
    print(change_cnt-1)