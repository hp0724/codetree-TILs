N,K = map(int,input().split()) 
max_value = 0
arr = []
for _ in range(N):
    idx,alpha = input().split()
    max_value = max(int(idx),max_value)
    arr.append([idx,alpha])
position = [0] * (max_value + 1)

for a in arr:
    position_idx = a[0]
    position_idx = int(position_idx)
    position_alphabet = a[1]

    if position_alphabet == "G":
        position[position_idx] = 1
    elif position_alphabet == 'H':
        position[position_idx] = 2
result = 0
# 16 - 6 = 10
if len(position) <= K:
    result = sum(position)
else:
    for i in range(0,len(position)-K):
        temp = 0
        for j in range(i,i+K+1):
            temp += position[j]
        result = max(result,temp)

print(result)