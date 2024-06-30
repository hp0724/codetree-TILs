#  홀수 번째의 원소가 주어질 때마다
#  지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성해보세요
n = int(input())
array = list(map(int,input().split()))
result_array = []
for i in range(len(array)):
    result_array.append(array[i])
    if i % 2 == 0:
        result_array.sort()
        print(result_array[len(result_array)//2],end=" ")