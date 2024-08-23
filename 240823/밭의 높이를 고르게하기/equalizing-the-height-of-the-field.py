def min_cost_to_equalize_height(N, H, T, heights):
    min_cost = float('inf')

    for i in range(N - T + 1):
        cost = 0
        for j in range(T):
            cost += abs(heights[i + j] - H)
        min_cost = min(min_cost, cost)

    return min_cost

# 입력 예제
N, H, T = map(int, input().split())
heights = list(map(int, input().split()))

# 최소 비용 계산
result = min_cost_to_equalize_height(N, H, T, heights)
print(result)