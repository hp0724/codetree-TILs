def odd_even_sum(n):
    if n == 1 or n == 2 :
        return n 
    if n % 2 == 0:
        return odd_even_sum(n-2) + n 

    elif n%2 != 0:
        return odd_even_sum(n-2) + n  

n = int(input())
print(odd_even_sum(n))