# N개의 숫자로 이루어진 수열 A와 
# M개의 숫자로 이루어진 수열 B 
# 수열 B의 각 원소들의 순서를 바꿔 나오는 수열을 아름다운 수열 
# 수열은 permutations 
# 조합은 combinations

from itertools import permutations

# N: A_arr의 길이, M: B_arr의 길이
N, M = map(int, input().split())

# A_arr와 B_arr 입력 받기
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

cnt = 0  # 일치하는 부분 배열의 개수를 세는 변수
permu_arr = []

# B_arr의 모든 순열을 생성
for p in permutations(B_arr, len(B_arr)):
    permu_arr.append(list(p))

# A_arr에서 부분 배열을 찾기 위한 루프
for i in range(N - M + 1):
    # A_arr의 부분 배열과 B_arr의 순열들을 비교
    if A_arr[i:i + M] in permu_arr:
        cnt += 1

print(cnt)