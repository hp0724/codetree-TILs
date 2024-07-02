month_day = [31,29,31,30,31,30,31,31,30,31,30,31]
day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
m1,d1,m2,d2 = map(int,input().split())
input_day_of_the_week = input()

for idx,value in enumerate(day_of_the_week):
    if input_day_of_the_week == value:
        result = idx 

# 월요일 부터 입력 요일 까지 값 빼고 
# 일주일 나누기 
count = 0
sum_day = (sum(month_day[:m2]) + d2) - (sum(month_day[:m1]) + d1)
if sum_day - result > 0:
    sum_day -= result 
    count += 1
    if sum_day >= 7:
        count += sum_day // 7

print(count)