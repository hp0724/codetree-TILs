# 숫자 N과 문자열이 주어지면 그 문자열에서 ‘C', ‘O’, 그리고 ‘W’ 가 순서대로 몇번 나오는지 세고싶어합니다. 
n = int(input())
input_str = input()

cnt = 0
for i in range(len(input_str)-2):
    for j in range(i,len(input_str)-1):
        for k in range(j,len(input_str)):
            if input_str[i] == 'C' and input_str[j] == 'O' and input_str[k] == 'W':
                cnt += 1 

print(cnt)