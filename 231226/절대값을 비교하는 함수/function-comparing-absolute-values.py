n=int(input())

for _ in range(n):
    a,b=map(int,input().split())
    a=abs(a)
    b=abs(b)
    if a<b:
        print(abs(b))
    else:
        print(abs(a))