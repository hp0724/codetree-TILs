# 개발자 6명의 알고리즘 능력을 수치화해 각각 정수로 주어지면 6명을 2명씩 3팀으로 배정 
# 10 18 8

arr = list(map(int,input().split()))

def sum_diff(i,j,k,l):
    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) - sum1 -sum2

    return (max(sum1,sum2,sum3) - min(sum1,sum2,sum3))


min_diff = 1e6 

for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            for l in range(len(arr)):
                if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                    min_diff = min(min_diff,sum_diff(i,j,k,l))


print(min_diff)