# n개의 숫자가 주어지고, 정확히 서로 다른 3개의 숫자를 골랐을때 carry 가 전형 발생하지 않으면서 나올수 있는 숫자 합의 최댓값 
# 각자리수를 모두 각각 더하는 경우 10 이상이 되는 경우가 전혀 없을 때 
# 모든 숫자쌍에서 carry 가 발생하는 경우 -1 
# carry 발생하지 않으면서 3개의 숫자의 최대 합을 출력 

# 1 <= 숫자의 범위 <= 10,000 
# 어떻게 하면 자릿수마다 더하기가 가능 ?? 

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

ans = -1 
for i in range(n): 
    for j in range(i+1,n):
        for k in range(j+1,n):
            carry = False 

            # 일의 자리에서 carry 발생 
            if arr[i] % 10 + arr[j] % 10 + arr[k] % 10 >= 10:
                carry = True 
            
            # 십의 자리에서 carry 발생
            if arr[i] % 100 //10 + arr[j] % 100 //10 + arr[k] % 100 //10 >= 10:
                carry = True
            
            # 백의 자리에서 carry 발생
            if arr[i] % 1000 //100 + arr[j] % 1000 //100 + arr[k] % 1000 //100 >= 10:
                carry = True
            
            # 천의 자리에서 carry 발생
            if arr[i] % 10000 //1000 + arr[j] % 10000 //1000 + arr[k] % 10000 //1000 >= 10:
                carry = True
            
            if carry == False:
                ans = max(ans,arr[i] + arr[j] + arr[k])

print(ans)