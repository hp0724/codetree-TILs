# 1 ~ N 까지의 숫자를 이용해 3자리 만들어야 하는 3단 다이얼 
# 1 과 N이 인접한 원형으로 된 자물쇠 
# 모든 자리에 대해 첫번째 조합과 거리가 2 이내 두번째 조합과 거리가 2 이내 
# 자물쇠가 열리게 되는 서로 다른 조합의 수를 구하는 프로그램을 작성해보세요

n = int(input())
a,b,c = list(map(int,input().split()))
a2,b2,c2 = list(map(int,input().split()))

cnt = 0 

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if (abs(a-i) <= 2 or abs(a-i) >= n-2) and (abs(b-j) <= 2 or abs(b-j) >= n-2 ) and (abs(c-k) <= 2 or abs(c-k) >= n-2 ):
                cnt += 1 
            elif (abs(a2-i) <= 2 or abs(a2-i) >= n-2) and (abs(b2-j) <= 2 or abs(b2-j) >= n-2 ) and (abs(c2-k) <= 2 or abs(c2-k) >= n-2 ):
                cnt += 1 

print(cnt)