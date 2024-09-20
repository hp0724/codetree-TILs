n,t = map(int,input().split())

# 124593651 
# 112459365
 
first_arr = list(map(int,input().split()))
second_arr = list(map(int,input().split()))
third_arr = list(map(int,input().split()))

repeat_count = 3 

total_arr = []

for i in first_arr:
    total_arr.append(i)

for j in second_arr:
    total_arr.append(j)

for k in third_arr:
    total_arr.append(k)



for _ in range(t):
    temp = total_arr[repeat_count*n-1]

    for l in range(n*repeat_count-1,0,-1):
        total_arr[l] = total_arr[l-1]
    
    total_arr[0] = temp 

print(" ".join(map(str,total_arr[:n])))
print(" ".join(map(str,total_arr[n:2*n])))
print(" ".join(map(str,total_arr[2*n:])))