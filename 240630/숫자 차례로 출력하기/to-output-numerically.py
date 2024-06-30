def print_number(n):
    if n == 0:
        return 
    print_number(n-1)
    print(n,end=" ")

def print_number_reverse(n):
    if n == 0:
        return 
    print(n,end=" ")
    print_number_reverse(n-1)

n = int(input())
print_number(n)
print()
print_number_reverse(n)