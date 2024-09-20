# 시계방향 컨베이어 벨트 
n,t = map(int,input().split())

 
arr = []
first_arr = list(map(int,input().split()))
second_arr = list(map(int,input().split()))


total_arr = []

for i in first_arr:
    total_arr.append(i)

for j in second_arr:
    total_arr.append(j)


for _ in range(t):
    temp = total_arr[2*n-1]

    for k in range(n*2-1,0,-1):
        total_arr[k] = total_arr[k-1]
    
    total_arr[0] = temp 

print(" ".join(map(str,total_arr[:n])))
print(" ".join(map(str,total_arr[n:])))