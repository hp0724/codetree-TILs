a,b = map(int,input().split())
n = input()
a_to_10 = int(n,a)

result = ''
while a_to_10 > 0:
    a_to_10,mod = divmod(a_to_10,b)
    result += str(mod) 

print(result[::-1])