# n 짝수면 2 
# n 홀수면 3 

def until_1(n):
    global cnt 
    if n == 1:
        return  
    if n % 2 == 0:
        cnt += 1 
        until_1(n//2)
    if n % 2 != 0:
        cnt += 1 
        until_1(n//3)
cnt = 0 
n = int(input())
until_1(n)
print(cnt)