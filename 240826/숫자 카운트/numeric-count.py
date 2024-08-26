# 1. A 가 생각한 세자리 수의 동일한 자리에 위치한다면 1 번 카운트 
# 2. A가 생각한 세자리 수에 있긴 하나 다른 자리에 위치하면 2번 카운트 
# 가능한 경우의 수 
# 서로 다른 숫자 세 개
#  (1 0) (2 0) (3 0) (1 1) (1 2) (2 1) (0 1)(0 2) (0 3)
n = int(input())
arr = []
for _ in range(n):
    number,count1,count2 = map(int,input().split())
    arr.append([number,count1,count2])
cnt = 0 
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            # 서로 다른 숫자 세개 인지 확인 
            if i == j or j == k or k == i:
                continue
            
            # 해당 숫자가 정답일때 , 모든 입력에 대해 올바른 답이 나오는지 확인 
            succeeded = True 

            for a,num_cnt1,num_cnt2 in arr:
                # 자릿수 분리 
                x = a // 100 
                y = a // 10 % 10 
                z = a % 10 

                cnt1 = 0 
                cnt2 = 0 
                
                if x == i:
                    cnt1 += 1
                if y == j:
                    cnt1 += 1
                if z == k:
                    cnt1 += 1
                if x == j or x == k:
                    cnt2 += 1 
                if y == i or y == k:
                    cnt2 += 1
                if z == i or z == j:
                    cnt2 += 1 
                
                # 카운트 수가 다른경우 정답 x 
                if cnt1 != num_cnt1 or cnt2 != num_cnt2:
                    succeeded = False 
                    break 
            if succeeded:
                cnt += 1 
            
print(cnt)