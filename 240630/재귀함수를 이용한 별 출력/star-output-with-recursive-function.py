def print_start(n):
    if n == 0: 
        return 
    print_start(n-1)
    print("*"*n)

n = int(input())
print_start(n)