def split_sum_value(n):
    if n <10:
        return n 
    return split_sum_value(n//10) + (n % 10)

array = list(map(int,input().split()))
result = array[0]
for i in range(1,len(array)):
    result *= array[i]

print(split_sum_value(result))