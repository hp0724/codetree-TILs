MAX_NUM = 100 

n = int(input())
# dp 처럼 우선 만들어두기 
arr = [0] * (MAX_NUM + 1) 

for _ in range(n):
    x,c = input().split()
    x = int(x)

    if c == 'G':
        arr[x] = 1 
    elif c== 'H':
        arr[x] = 2

max_len = 0 
for i in range(MAX_NUM+1):
    for j in range(i+1,MAX_NUM+1):
        # i 와 j 위치에 사람이 있는지 확인 
        if arr[i] == 0 or arr[j] == 0:
            continue
        
        cnt_g = 0
        cnt_h = 0
        
        for k in range(i,j+1):
            if arr[k] == 1:
                cnt_g += 1 
            if arr[k] == 2:
                cnt_h += 1 
        
        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            length = j - i 
            max_len = max(max_len,length)

print(max_len)