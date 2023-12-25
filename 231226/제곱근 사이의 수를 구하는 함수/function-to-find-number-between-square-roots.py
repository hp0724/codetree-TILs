a,b=map(float,input().split())
a=int(a**(1/2))
b=int(b**(1/2))

if a<b:
    print(b-a)
else:
    print(a-b)