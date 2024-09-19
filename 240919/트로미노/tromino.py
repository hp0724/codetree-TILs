# 블럭은 자유롭게 회전하거나 뒤집을 수 있습니다.
# 블럭 L는 4가지 방법  
# **   *    **   *
#  *   **   *   **
# 블럭 l 는 2가지 방법 
n,m = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

# **
#  *
max_cnt_1 = 0 
for i in range(n-1):
    for j in range(m-1):
        max_cnt_1 = max(max_cnt_1,arr[i][j] + arr[i][j+1] + arr[i+1][j+1]) 

# **
# *
max_cnt_2 = 0 
for i in range(n-1):
    for j in range(m-1):
        max_cnt_2 = max(max_cnt_2,arr[i][j] + arr[i][j+1] + arr[i+1][j]) 

# *
# **
max_cnt_3 = 0 
for i in range(n-1):
    for j in range(m-1):
        max_cnt_3 = max(max_cnt_3,arr[i][j] + arr[i+1][j] + arr[i+1][j+1]) 

#  *
# **
max_cnt_4 = 0 
for i in range(n-1):
    for j in range(m-1):
        max_cnt_4 = max(max_cnt_4,arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1])

#  *
#  *
#  *
max_cnt_5 = 0 
for i in range(n-2):
    for j in range(m):
        max_cnt_5 = max(max_cnt_5,arr[i][j] + arr[i+1][j] + arr[i+2][j])

#  ***
max_cnt_6 = 0 
for i in range(n):
    for j in range(m-2):
        max_cnt_6 = max(max_cnt_6,arr[i][j] + arr[i][j+1] + arr[i][j+2])

total_max_cnt = max(max_cnt_1,max_cnt_2,max_cnt_3,max_cnt_4,max_cnt_5,max_cnt_6)

print(total_max_cnt)