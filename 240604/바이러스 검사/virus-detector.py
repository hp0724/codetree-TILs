# n개의 식당에 있는 고객들의 체온 측정 
# 검사팅장과 검사팀원으로 나누어진다. 
# 팀장과 팀원이 검사할수 있는 고객의 수가 다르다 
# 한 가게당 팀장은 오직 한명, 팀원은 여러명 
# 가게당 팀장 한 명은 무조건 필요하다. 
# n개의 식당 고객들의 체온을 측정하기 위해 필요한 검사자 수의 최솟값 

# 식당 수 n 
# 식당에 있는 고객의 수 
# 검사팀장이 검사할수 있는 최대 고객 수 
# 검사팀원이 검사할수 있는 최대 고객 수 

import sys
from collections import deque
input = sys.stdin.readline
restaurant = int(input())
customer = deque(list(map(int,input().split())))
leader,member = map(int,input().split())
cnt = 0 

while customer:
    temp = customer[0]
    temp -= leader
    cnt +=1
    if temp >0: 
        cnt += (temp // member)
        if temp % member !=0:
            cnt += 1

    customer.popleft()    

print(cnt)