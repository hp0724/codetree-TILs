#  "x L"의 경우 왼쪽으로 이동하면서 현재 위치 타일포함 총 x칸의 타일을 흰색으로 연속하게 칠하고
# "x R"의 경우 오른쪽으로 이동하면서 현재 위치 타일포함 총 x칸의 타일을 검은색으로 연속하게 칠함
#  타일의 색은 덧칠해지면 마지막으로 칠해진 색으로 바뀌는데
# 타일 하나가 순서 상관없이 흰색과 검은색으로 각각 두 번 이상 칠해지면 회색으로 바뀌고 더 이상 바뀌지 않습니다.

N_MAX = 1000
X_MAX = 100 
color_array = [0] * (N_MAX * X_MAX * 2)
color_white_array = [0] * (N_MAX * X_MAX * 2)
color_black_array = [0] * (N_MAX * X_MAX * 2)
count_array = [0] * (N_MAX * X_MAX * 2)
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
            color_white_array[i] += 1
        cur -= c
        
    # 오른쪽이면 현재 포함 검정색(2)으로 색칠 
    elif d == "R":
        for i in range(cur,cur+c+1):
            color_array[i] = 2
            color_black_array[i] += 1
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
gray = 0
for i in range(len(count_array)):
    if color_black_array[i] >=2 and color_white_array[i] >=2 :
        gray += 1
    else:
        if color_array[i] !=0:
            if color_array[i] == 1:
                white += 1
            elif color_array[i] == 2:
                black += 1

print(white,black,gray)