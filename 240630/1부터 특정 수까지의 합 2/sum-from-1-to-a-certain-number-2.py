def sum_value(n):
    if n == 0:
        return 0
    return n + sum_value(n-1)

n = int(input())
print(sum_value(n))