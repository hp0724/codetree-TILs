# 1 부터 N 까지 숫자를 중복해서 뽑아 총 3자리 
# 총 조합의 수에서 안열리는 수 빼는것이 좋을듯 

N = int(input())
arr = list(map(int,input().split()))

cnt = 0 
total_combi = N*N*N 

cnt = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if  (i < arr[0]-2  or  i > arr[0] +2) and (j < arr[1]-2  or j > arr[1] +2)  and (k < arr[2]-2  or  k > arr[2] +2):
                # print(i,j,k)
                cnt += 1 
 
print(total_combi-cnt)