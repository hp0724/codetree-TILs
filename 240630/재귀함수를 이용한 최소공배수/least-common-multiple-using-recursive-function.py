def least(a, b):
    A, B = a, b
    while b > 0:
        a, b = b, a % b
    return A * B // a

# arr에서 앞 2개씩 접근하면서 최소공배수 갱신
def solution(arr):
    arr.sort()
    temp = arr[0]
    for i in range(0, len(arr)-1):
        temp = least(temp, arr[i+1])
    return temp

n = int(input())
array = list(map(int,input().split()))

print(solution(array))