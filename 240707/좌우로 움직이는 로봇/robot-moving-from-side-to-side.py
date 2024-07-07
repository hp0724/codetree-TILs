n,m = map(int,input().split())

a_input_arr = []
b_input_arr = []
a_result_arr = [0]
b_result_arr = [0]
for _ in range(n):
    cnt,direction = input().split()
    a_input_arr.append((int(cnt),direction))
for _ in range(m):
    cnt,direction = input().split()
    b_input_arr.append((int(cnt),direction))


for c,d in a_input_arr:
    if d == "L":
        for i in range(c):
            a_result_arr.append(a_result_arr[-1]-1)
    elif d == "R":
        for i in range(c):
            a_result_arr.append(a_result_arr[-1]+1)

for c,d in b_input_arr:
    if d == "L":
        for i in range(c):
            b_result_arr.append(b_result_arr[-1]-1)
    elif d == "R":
        for i in range(c):
            b_result_arr.append(b_result_arr[-1]+1)

cnt = 0 
if len(a_result_arr) > len(b_result_arr):
    for i in range(len(a_result_arr)-len(b_result_arr)):
        b_result_arr.append(b_result_arr[-1])
elif len(b_result_arr) > len(a_result_arr):
    for i in range(len(b_result_arr)-len(a_result_arr)):
        a_result_arr.append(a_result_arr[-1])

for idx in range(1,len(a_result_arr)):
    if a_result_arr[idx] == b_result_arr[idx] and a_result_arr[idx-1] != b_result_arr[idx-1]:
        cnt += 1

print(cnt)