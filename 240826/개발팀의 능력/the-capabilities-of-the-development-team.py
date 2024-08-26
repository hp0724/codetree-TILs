# 최대 능력의 팀과 최소 능력의 팀간의 능력 차이중 가능한 최솟값 
arr = list(map(int,input().split()))


def sum_diff(i,j,k,l):

    sum1 = arr[i] + arr[j]
    sum2 = arr[k] + arr[l]
    sum3 = sum(arr) -sum1 -sum2

    if (sum1!= sum2 and sum1!=sum3 and sum2!=sum3):
        return max(sum1,sum2,sum3) - min(sum1,sum2,sum3)
    return 1e6
    
min_diff = 1e6 

for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            for l in range(len(arr)):
                if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l: 
                    min_diff = min(min_diff,sum_diff(i,j,k,l))


if min_diff == 1e6:
    print(-1)
else:
    print(min_diff)