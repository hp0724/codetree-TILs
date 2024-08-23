# 입력 예제
N, H, T = map(int, input().split())
heights = list(map(int, input().split()))

min_cost = 1e6

for i in range(N - T + 1):
    cost = 0
    for j in range(T):
        cost += abs(heights[i + j] - H)
    min_cost = min(min_cost, cost)

print(min_cost)