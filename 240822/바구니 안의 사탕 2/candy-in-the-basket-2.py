# N개의 바구니 k 의 간격
# 바구니 안에 사탕 
# 중심점 C를 잡기 
# 사탕의 개수와 바구니 좌표 

N,K = map(int,input().split())
arr = []
max_idx = 0
for _ in range(N): 
    cnt,idx = map(int,input().split())
    arr.append([cnt,idx])
    max_idx = max(max_idx,idx)

placed = [0] * (max_idx+1) 

for cnt,idx in arr:
    if placed[idx] != 0:
        placed[idx] += cnt 
    else:
        placed[idx] = cnt 

result = 0 
if 2*K >= max_idx:
    result = sum(placed)
else:
    for i in range(max_idx - 2*K+1): 
        result = max(result,sum(placed[i:i+2*K+1]))

print(result)