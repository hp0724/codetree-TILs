def change_N(N,B):
    rev_base = ''
    while N > 0:
        N,mod = divmod(N,B)
        rev_base += str(mod)
    
    return rev_base[::-1]

N,B = map(int,input().split())
print(change_N(N,B))