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
input = sys.stdin.readline
restaurant = int(input())
customer = []
for _ in range(restaurant):
    customer.append(int(input()))
leader,member = map(int,input().split())


print(customer)