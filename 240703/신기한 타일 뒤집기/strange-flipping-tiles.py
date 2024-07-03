#왼쪽으로 뒤집으면 흰색으로 바뀌고, 
#오른쪽으로 뒤집으면 검은색으로 바뀌게 됩니다.
#현재 위치 타일포함현재 위치 타일포함

N_MAX = 1000
X_MAX = 100 
color_array = [0] * (N_MAX * X_MAX * 2)
offset = N_MAX * X_MAX 

direction_array = []

n = int(input())
for _ in range(n):
    direction_array.append(tuple(input().split()))

cur = offset
for c,d in direction_array:
    c = int(c) - 1
    # 왼쪽이면 현재 포함 흰색(1)으로 색칠 
    # print(cur)
    if d == "L":
        for i in range(cur-c,cur+1):
            color_array[i] = 1
        cur -= c
        
    # 오른쪽이면 현재 포함 검정색(2)으로 색칠 
    elif d == "R":
        for i in range(cur,cur+c+1):
            color_array[i] = 2
        cur += c 
        
    # print("현재색깔")
    # print(color_array[99990:100010])
    # print("흰 색깔 개수")
    # print(color_white_array[99990:100010])
    # print("검정 색깔 개수")
    # print(color_black_array[99990:100010])
    # print()

    

white = 0
black = 0 
for i in range(len(color_array)):
    if color_array[i] !=0:
        if color_array[i] == 1:
            white += 1
        elif color_array[i] == 2:
            black += 1

print(white,black)