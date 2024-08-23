#  N개의 밭의 높이가 주어지면 연속하게 최소 T번 이상 H높이로 나오게끔 하려고 할 때
N,H,T = map(int,input().split())

arr = list(map(int,input().split()))

min_value = 1e6
for i in range(N-T+1):
    temp = 0
    for j in range(T):
        temp += abs(H-arr[k])
    min_value = min(min_value,temp)

print(min_value)

# # 입력 예제
# N, H, T = map(int, input().split())
# arr = list(map(int, input().split()))

# min_cost = 1e6

# for i in range(N - T + 1):
#     cost = 0
#     for j in range(T):
#         cost += abs(arr[i + j] - H)
#     min_cost = min(min_cost, cost)

# print(min_cost)