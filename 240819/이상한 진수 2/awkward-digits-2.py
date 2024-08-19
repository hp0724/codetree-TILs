# 0 이상의 정수 N을 2진법으로 나타낸 뒤, 
# 그 숫자들 중 정확히 한 숫자만을 바꾼 숫자 a가 주어졌을 때, 
# 가능한 숫자 N 중 최댓값을 찾는 프로그램을 작성해보세요.
# 1111

input_value = list(map(int,input()))
if len(input_value) == input_value.count(1):
    input_value[-1] = 0
else:
    for i in range(len(input_value)):
        if input_value[i] == 0:
            input_value[i] = 1
            break
input_value = "".join(map(str,input_value))
# input_value = " ".join(input_value)
print(int(input_value,2))