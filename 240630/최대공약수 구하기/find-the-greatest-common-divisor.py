def gcd(n1,n2):
    min_value = min(n1,n2)
    for i in range(min_value,-1,-1):
        if n1 % i ==0 and n2 % i ==0:
            return i

n,m = map(int,input().split())
print(gcd(n,m))