n = int(input())
array = []
for i in range(n):
    w,h = map(int,input().split())
    array.append((w,h,i+1))

array.sort(key=lambda x:(x[0],-x[1]))
for arr in array:
    print(" ".join(map(str,arr)))