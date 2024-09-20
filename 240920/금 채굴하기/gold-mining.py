# 마름모의 정의를 사용하자 
# 중심저을 기준으로 중심 에서 x거리의 + 중심에서 y거리 차이 <= k 이면 포함되어있음 

n,m = map(int,input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

# k에 대하여 마름모의 넓이 반환 
def get_area(k):
    return k*k + (k+1) * (k+1)

def get_num_of_gold(row,col,k):
    result = 0
    for i in range(n):
        for j in range(n):
            # 맨해튼 거리가 k 이하인 경우
            if abs(row - i) + abs(col - j) <= k:
                result += arr[i][j] 
    
    return result

max_gold = 0 

# k의 최대 범위 
for row in range(n):
    for col in range(n): 
        for k in range(2*(n-1) +1):
            num_of_gold = get_num_of_gold(row,col,k)

            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold,num_of_gold)

print(max_gold)